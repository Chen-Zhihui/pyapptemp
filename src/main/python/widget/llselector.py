from qtpy.QtWidgets import QLabel, QFrame, QComboBox, QHBoxLayout
import qtpy.QtGui as QtGui
from qtpy.QtCore import Signal, QPoint, Qt

import numpy as np
from main.python.widget.helper import plain_frame
import logging

def fix_width(w):
    w.setMaximumWidth(100)
    w.setMinimumWidth(100)

class LonSelector(QFrame):
    
    def __init__(self, parent=None) -> None:
        super(QFrame, self).__init__(parent)
        self._init_layout()
        self._init_data()
        self.setCurrentIndex = self._num.setCurrentIndex

    def _init_layout(self):
        plain_frame(self)
        self._layout = QHBoxLayout(self)
        self._name = QLabel("经度", self)
        self._layout.addWidget(self._name)
        self._separator = QLabel(":", self)
        self._layout.addWidget(self._separator)
        self._num = QComboBox(self)
        fix_width(self._num)
        self._layout.addWidget(self._num)
        self._dot = QComboBox(self)
        fix_width(self._dot)
        self._layout.addWidget(self._dot)

        self._layout.addStretch()

    def _init_data(self):
        n = np.linspace(-180, 180, 361)
        d = np.linspace(0, 1.0, 5)
        for nv in n:
            self._num.addItem(str(int(nv)))
        for nd in d[0:-1]:
            self._dot.addItem(str(nd))
        self._num.setCurrentIndex(180)

    def getValue(self):
        return (int(self._num.currentData(Qt.DisplayRole)) +   
                float(self._dot.currentData(Qt.DisplayRole)))


class LatSelector(QFrame):
    
    def __init__(self, parent=None) -> None:
        super(QFrame, self).__init__(parent)
        self._init_layout()
        self._init_data()
        self.setCurrentIndex = self._num.setCurrentIndex

    def _init_layout(self):
        plain_frame(self)
        self._layout = QHBoxLayout(self)
        self._name = QLabel("纬度", self)
        self._layout.addWidget(self._name)
        self._separator = QLabel(":", self)
        self._layout.addWidget(self._separator)
        self._num = QComboBox(self)
        fix_width(self._num)
        self._layout.addWidget(self._num)
        self._dot = QComboBox(self)
        fix_width(self._dot)
        self._layout.addWidget(self._dot)
        self._layout.addStretch()

    def _init_data(self):
        n = np.linspace(-90, 90, 181)
        d = np.linspace(0, 1.0, 5)
        for nv in n:
            self._num.addItem(str(int(nv)))
        for nd in d[0:-1]:
            self._dot.addItem(str(nd))

        self._num.setCurrentIndex(90)

    def getValue(self):
        return (int(self._num.currentData(Qt.DisplayRole)) +   
                float(self._dot.currentData(Qt.DisplayRole)))
