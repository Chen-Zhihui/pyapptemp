import logging
logging.info(f"{__file__}")

from main.python.widget import (
    zero_space, plain_frame, create_vline, create_hline,
    icon_button
)

import typing 

import qtawesome as qta

import qtpy.QtCore as QtCore
from qtpy.QtWidgets import (
    QWidget, 
    QFrame, 
    QToolBar, 
    QAction, 
    QSplitter,
    QTextEdit,
    QFileSystemModel,
    QTreeView,
    QTableWidget,
    QTableWidgetItem,
    QPushButton,
    QMenuBar,
    QGroupBox,
    QCheckBox,
    QComboBox,
    QButtonGroup,
    QTableView,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QFileDialog
)

class TempView(QFrame):

    def __init__(self, parent) -> None:
        super().__init__(parent)
        self._init_window_info()
        self._init_layout()
        self._init_actions()
        self._init_data()

    def _init_window_info(self):
        self.setWindowIcon(qta.icon('mdi.view-list',
                color='blue',
                color_active='orange',
                opacity=0.7))
        self.setWindowTitle("模板视图")   

    def _init_layout(self):
        plain_frame(self)
        
    def _init_actions(self):
        pass

    def _init_data(self):
        pass