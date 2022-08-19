import logging
logging.info(f"{__file__}")

import qtawesome as qta
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
    QMenuBar
)

def icon_button(name, icon=None, parent=None):
    btn = QPushButton(name, parent=parent)
    btn.setMinimumSize(200, 40)
    if icon:
        btn.setIcon(qta.icon(icon,
                color='blue',
                color_active='orange',
                opacity=0.7))
    return btn