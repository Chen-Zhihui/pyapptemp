from main.python.widget import zero_space, plain_frame, Box, TableBox, create_hline, create_vline

from qtpy.QtWidgets import (
    QDoubleSpinBox, 
    QLabel, 
    QFrame, 
    QHBoxLayout, 
    QVBoxLayout,
    QFrame,
    QSplitter,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QAbstractItemView
)
from qtpy.QtCore import ( 
    QDateTime,
    QModelIndex,
    Qt,
    QRect,
    QSize,
    Signal,
)

class ListView(QTableWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.targets = []
        self.title = "Title"
        self.setColumnCount(1)

    def setTitle(self, title):  
        self.title = title      
        self.setHorizontalHeaderItem(0, QTableWidgetItem(title))
        self.horizontalHeader().setStretchLastSection(True)

    def clearItem(self):
        self.setRowCount(0)        

    def fillItem(self, tl):
        self.clear()
        self.setTitle(self.title)
        self.targets = tl 
        self.setRowCount(len(tl))
        i = 0
        for t in tl :
            self.setItem(i, 0, QTableWidgetItem(str(t)))       
            i += 1

    def addItem(self, i):
        self.setRowCount(self.rowCount()+1)
        self.setItem(self.rowCount()-1, 0, QTableWidgetItem(str(i)))