from qtpy.QtCore import QThread, QObject, QEvent


class CallbackEvent(QEvent):
    typeid = QEvent.User + 1

    def __init__(self, cb=None):
        super().__init__(CallbackEvent.typeid)
        if cb:  #is not None:
            self.cb = cb
        else:
            self.cb = lambda x: x


class EventSpy(QObject):

    def __init__(self, target: QObject = None, cb=None, parent=None):
        QObject.__init__(self, parent=parent)
        self.target = target
        self.cb = cb

    def eventFilter(self, watched: QObject, ev: QEvent):
        if watched is self.target and isinstance(ev, CallbackEvent):
            if self.cb:
                self.cb(ev)
                return True
        return super().eventFilter(watched, ev)

    def event(self, ev: QEvent):
        if isinstance(ev, CallbackEvent):
            ev.cb()
            return True
        else:
            return super().event(ev)


