from .event import EventSpy, CallbackEvent
from typing import Any, Optional, Set
from rx.core import typing
from rx.disposable import CompositeDisposable, Disposable, SingleAssignmentDisposable
from rx.scheduler.periodicscheduler import PeriodicScheduler
from qtpy.QtCore import QObject, QEvent, Signal
import rx


class EventFilter(QObject):

    def __init__(self, parent, subscriber):
        super().__init__(parent=parent)
        self._subscriber = subscriber

    def eventFilter(self, obj: QObject,  ev: QEvent):
        self._subscriber.on_next(ev)
        return super().eventFilter(obj, ev)

    def __del__(self):
        self._subscriber.on_completed()


def from_event(obj: QObject):
    if not obj or not isinstance(obj, QObject):
        return rx.never()
    if not hasattr(obj, "___rx_subject_qevent"):
        ev_sub = rx.subject.Subject()
        setattr(obj, "___rx_subject_qevent", ev_sub)
        event_filter = EventFilter(obj, ev_sub)
        setattr(obj, "___rx_qevent_listener", event_filter)
        obj.installEventFilter(event_filter)
    assert obj.___rx_subject_qevent
    return obj.___rx_subject_qevent

def from_signal(sig: Signal):
    def my(obs, disp):
        def cb(*args):
            if len(args)>0:
                obs.on_next(*args)
            else:
                obs.on_next(None)
        sig.connect(cb)
    return rx.create(my)

class QtUiScheduler(PeriodicScheduler):
    """A scheduler for a PyQt5/PySide2 event loop."""

    @staticmethod
    def process_in_ui(ev):
        ev.cb()

    def __init__(self, qtcore: Any, qApplication: Any):
        """Create a new QtUiScheduler.

        Args:
            qtcore: The QtCore instance to use; typically you would get this by
                either import qtpy.QtCore or import PySide2.QtCore
        """
        super().__init__()
        self._qtcore = qtcore
        timer_class: Any = self._qtcore.QTimer
        self._periodic_timers: Set[timer_class] = set()

        self._qtApp = qApplication
        self._spy = EventSpy(qApplication, QtUiScheduler.process_in_ui)
        self._qtApp.installEventFilter(self._spy)

    def schedule(self,
                 action: typing.ScheduledAction,
                 state: Optional[typing.TState] = None
                 ) -> typing.Disposable:
        """Schedules an action to be executed.

        Args:
            action: Action to be executed.
            state: [Optional] state to be given to the action function.

        Returns:
            The disposable object used to cancel the scheduled action
            (best effort).
        """
        return self.schedule_relative(0.0, action, state=state)

    def schedule_relative(self,
                          duetime: typing.RelativeTime,
                          action: typing.ScheduledAction,
                          state: Optional[typing.TState] = None
                          ) -> typing.Disposable:
        """Schedules an action to be executed after duetime.

        Args:
            duetime: Relative time after which to execute the action.
            action: Action to be executed.
            state: [Optional] state to be given to the action function.

        Returns:
            The disposable object used to cancel the scheduled action
            (best effort).
        """
        msecs = max(0, int(self.to_seconds(duetime) * 1000.0))
        sad = SingleAssignmentDisposable()
        is_disposed = False

        def invoke_action() -> None:
            if not is_disposed:
                sad.disposable = action(self, state)

        def proxy() -> None:
            # nonlocal is_disposed
            if not is_disposed:
                sad.disposable = action(self, state)

        def invoke_action2() -> None:
            if not is_disposed:
                self._qtApp.postEvent(self._spy, CallbackEvent(proxy))

        timer = None

        def start_timer():
            nonlocal timer
            timer = self._qtcore.QTimer()
            timer.setSingleShot(True)
            timer.timeout.connect(invoke_action2)
            timer.setInterval(msecs)
            self._periodic_timers.add(timer)
            timer.start()

        self._qtApp.postEvent(self._spy, CallbackEvent(start_timer))

        def dispose() -> None:
            timer.stop()
            self._periodic_timers.remove(timer)
            timer.deleteLater()
            pass

        return CompositeDisposable(sad, Disposable(dispose))

    def schedule_absolute(self,
                          duetime: typing.AbsoluteTime,
                          action: typing.ScheduledAction,
                          state: Optional[typing.TState] = None
                          ) -> typing.Disposable:
        """Schedules an action to be executed at duetime.

        Args:
            duetime: Absolute time at which to execute the action.
            action: Action to be executed.
            state: [Optional] state to be given to the action function.

        Returns:
            The disposable object used to cancel the scheduled action
            (best effort).
        """

        delta = self.to_datetime(duetime) - self.now
        return self.schedule_relative(delta, action, state=state)

    def schedule_periodic(self,
                          period: typing.RelativeTime,
                          action: typing.ScheduledPeriodicAction,
                          state: Optional[typing.TState] = None
                          ) -> typing.Disposable:
        """Schedules a periodic piece of work to be executed in the loop.

       Args:
            period: Period in seconds for running the work repeatedly.
            action: Action to be executed.
            state: [Optional] state to be given to the action function.

        Returns:
            The disposable object used to cancel the scheduled action
            (best effort).
        """
        msecs = max(0, int(self.to_seconds(period) * 1000.0))
        sad = SingleAssignmentDisposable()

        def proxy():
            nonlocal state
            state = action(state)

        def interval2():
            self._qtApp.postEvent(self._spy, CallbackEvent(proxy))

        def interval() -> None:
            nonlocal state
            state = action(state)

        timer = None

        def start_timer():
            nonlocal timer
            timer = self._qtcore.QTimer()
            timer.setSingleShot(not period)
            timer.timeout.connect(interval2)
            timer.setInterval(msecs)
            self._periodic_timers.add(timer)
            timer.start()

        self._qtApp.postEvent(self._spy, CallbackEvent(start_timer))

        def dispose() -> None:
            timer.stop()
            self._periodic_timers.remove(timer)
            timer.deleteLater()

        return CompositeDisposable(sad, Disposable(dispose))


