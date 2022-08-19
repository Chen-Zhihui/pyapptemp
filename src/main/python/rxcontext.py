import logging
logging.info("init rx")
logging.info(f"{__file__}")

from main.python.widget.event import CallbackEvent
from main.python.widget.event import EventSpy
from qtpy.QtCore import QEvent
import qtpy.QtCore
from qtpy.QtWidgets import QApplication
import rx
import rx.operators as ops

import functools
from rx.scheduler.threadpoolscheduler import ThreadPoolScheduler

from main.python.widget.rxtool import QtUiScheduler
QEvent.registerEventType(CallbackEvent.typeid)


gui_scheduler = QtUiScheduler(qtpy.QtCore, QApplication.instance())
thread_pool_scheduler = ThreadPoolScheduler()

def in_gui(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        rx.just(fn).pipe(
            ops.observe_on(gui_scheduler)
        ).subscribe(
            on_next=lambda f: f(*args, **kwargs),
            on_error = logging.info
        )
    return wrapper


def in_bg(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        rx.just(fn).pipe(
            ops.observe_on(gui_scheduler)
        ).subscribe(
            on_next=lambda f: f(*args, **kwargs),
            on_error = logging.info
        )
    return wrapper


def run_in_gui(fn):
    rx.just(fn).pipe(
        ops.observe_on(gui_scheduler)
    ).subscribe(
        on_next=lambda f: f()
    )