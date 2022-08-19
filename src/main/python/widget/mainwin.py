
from qtpy.QtWidgets import  QFrame, QVBoxLayout, QStackedLayout, QHBoxLayout
from qtpy.QtWidgets import  QSizePolicy, QToolButton, QWidget
from qtpy.QtCore import Qt, QSize
from qtpy.QtGui import QIcon
import typing
from .header import HeaderWidget
from .helper import zero_space, create_vline

class SideBar(QFrame) :

    def __init__(self, parent) -> None:
        super(SideBar, self).__init__(parent)
        self.leftNav = QVBoxLayout(self)
        zero_space(self.leftNav)
        self.leftNav.addStretch()
        self.btns = []

    def addButton(self, btn)->None:
        btn.setIconSize(QSize(50, 50))
        btn.setCheckable(True)
        btn.setMaximumHeight(100)
        btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.leftNav.insertWidget(self.leftNav.count()-1, btn)
        self.btns.append(btn)

    def clearOthers(self, btn):
        for b in self.btns:
            if b is not btn:
                b.setChecked(False)

    def setCurrent(self, index):
        assert index < len(self.btns)
        btn = self.btns[index]
        btn.click()


class MainWin(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.header = HeaderWidget()
        self.body = QWidget()
        self.layout = QVBoxLayout(self)
        zero_space(self.layout)
        self.layout.addWidget(self.header)
        self.layout.addWidget(self.body)

        self.sigAbout = self.header.sigAbout

        self.setIcon = self.header.setIcon
        self.setTitle = self.header.setTitle

        self.bodyLayout = QHBoxLayout(self.body)
        self.leftNavWdg = SideBar(self.body)
        self.leftNavWdg.setMinimumSize(150, 0)
        self.leftNavWdg.setMaximumSize(150, 3000)
        
        self.vLine = create_vline()        
        self.content = QStackedLayout()   
        zero_space(self.content)            
        self.bodyLayout.addWidget(self.leftNavWdg)
        self.bodyLayout.addWidget(self.vLine)
        self.bodyLayout.addLayout(self.content)
        zero_space(self.bodyLayout)


    def addPage(self, widget) :
        btn = QToolButton()
        btn.setText(widget.windowTitle())
        btn.setIcon(widget.windowIcon())
        self.leftNavWdg.addButton(btn)        
        index = self.content.addWidget(widget)
        self.content.setCurrentIndex(index)

        def clear_all():
            self.content.setCurrentIndex(index)
            self.leftNavWdg.clearOthers(btn)
            
        btn.clicked.connect(lambda b: clear_all())

    def setCurrent(self, index) -> None :
        self.leftNavWdg.setCurrent(index)


if __name__ == "__main__" :
    from qtpy.QtWidgets import QApplication
    import os
    import sys

    app = QApplication(sys.argv)
    w = MainWin()
    w.addPage("title", QIcon(), QWidget())
    w.addPage("title", QIcon(), QWidget())
    w.addPage("title", QIcon(), QWidget())
    w.resize(1000, 800)
    w.show()
    app.exec_()