from main.python.widget import zero_space, plain_frame
import qtawesome as qta
from qtpy.QtWidgets import (
    QWidget, 
    QFrame, 
    QToolBar, 
    QAction, 
    QSplitter,
    QTextEdit,
    QFileSystemModel,
    QTableView,
    QTableWidget,
    QTableWidgetItem,
    QPushButton,
    QDoubleSpinBox,
    QComboBox,
    QSpinBox,
    QHBoxLayout,
    QLabel
)


def min_width(w, width):
    w.setMinimumWidth(width)

class LatRange(QFrame):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._init_layout()
        self._init_data()

    def _init_layout(self):
        plain_frame(self)
        layout = QHBoxLayout(self)
        layout.addStretch()
        zero_space(layout)
        self.lat_beg = QDoubleSpinBox(self)
        self.lat_end = QDoubleSpinBox(self)
        if "self.lat_layout" :
            layout.addWidget(QLabel("纬度: ", self))
            layout.addWidget(QLabel("从", self))
            layout.addWidget(self.lat_beg)
            layout.addWidget(QLabel("至", self))
            layout.addWidget(self.lat_end)

    def _init_data(self):
        for sb in [self.lat_beg, self.lat_end]:
            sb.setRange(-90, 90)
            min_width(sb, 80)

    def reset(self, min_, max_):
        self.lat_beg.setValue(min_)
        self.lat_end.setValue(max_)

    def range(self):
        return ( 
            min(self.lat_beg.value(), self.lat_end.value()),
            max(self.lat_beg.value(), self.lat_end.value())
        )

class LonRange(QFrame):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._init_layout()
        self._init_data()

    def _init_layout(self):
        plain_frame(self)
        layout = QHBoxLayout(self)
        layout.addStretch()
        zero_space(layout)
        self.lat_beg = QDoubleSpinBox(self)
        self.lat_end = QDoubleSpinBox(self)
        if "self.lat_layout" :
            layout.addWidget(QLabel("经度: ", self))
            layout.addWidget(QLabel("从", self))
            layout.addWidget(self.lat_beg)
            layout.addWidget(QLabel("至", self))
            layout.addWidget(self.lat_end)

    def _init_data(self):
        for sb in [self.lat_beg, self.lat_end]:
            sb.setRange(-180, 180)
            min_width(sb, 80)
    
    def reset(self, min_, max_):
        self.lat_beg.setValue(min_)
        self.lat_end.setValue(max_)

    def range(self):
        return ( 
            min(self.lat_beg.value(), self.lat_end.value()),
            max(self.lat_beg.value(), self.lat_end.value())
        )

