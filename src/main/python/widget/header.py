import string
from qtpy.QtWidgets import QLabel, QFrame, QToolButton, QHBoxLayout, QVBoxLayout
import qtpy.QtGui as QtGui
from qtpy.QtCore import Signal, QPoint
from qtpy.QtGui import QPixmap
import qtawesome as qta

class MoveHeader(QFrame) :

    moveBy = Signal(int, int)

    def __init__(self) -> None:
        self.last = None

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        self.last = a0.globalPos()
        super().mousePressEvent(a0)

    def mouseMoveEvent(self, a0: QtGui.QMouseEvent) -> None:
        dx = a0.globalX() - self.last.x()
        dy = a0.globalY() - self.last.y()
        self.last = a0.globalPos()
        super().mouseMoveEvent(a0)
        self.moveBy.emit(dx, dy)
        self.window().move(self.window().pos() + QPoint(dx, dy))

header_height = 60
content_margin = 0

class HeaderWidget(MoveHeader):

    def __init__(self) -> None:
        super(MoveHeader, self).__init__()
        self.setMaximumHeight(header_height)
        self.setMinimumHeight(header_height)

        self.hlayout = QHBoxLayout(self)
        self.hlayout.setSpacing(0)
        self.hlayout.setContentsMargins(10, content_margin, 10, content_margin)
        self.icon = QLabel()
        self.icon.setMaximumWidth(header_height - content_margin * 2)
        self.icon.setMinimumWidth(header_height - content_margin * 2)
        self.icon.setMaximumHeight(header_height - content_margin * 2)
        self.icon.setMinimumHeight(header_height - content_margin * 2)
        self.title = QLabel("Title")
        self.min = QToolButton()
        self.min.setIcon(qta.icon('fa5s.window-minimize',
                        color='darkblue',
                        color_active='orange' )
                        )
        self.min.clicked.connect(lambda : self.window().showMinimized())

        self.max = QToolButton()
        self.max.setIcon(qta.icon('fa5.window-maximize',
                        color='darkblue',
                        color_active='orange' )
        )
        self.max.clicked.connect(lambda : self.window().showMaximized())

        self.restore = QToolButton()
        self.restore.setIcon(qta.icon('fa5s.window-restore',
                        color='darkblue',
                        color_active='orange')
                        )
        self.restore.clicked.connect(lambda : self.window().showNormal())

        self.close = QToolButton()
        self.close.setIcon(qta.icon('fa5s.window-close',
                        color='darkblue',
                        color_active='orange')
                        )
        self.close.clicked.connect(lambda : self.window().close())

        self.about = QToolButton()
        self.about.setIcon(qta.icon("fa5s.info",
                        color='darkblue',
                        color_active='orange'
        ))

        self.hlayout.addWidget(self.icon)
        self.hlayout.addWidget(self.title)
        vlayout = QVBoxLayout()
        hlayout = QHBoxLayout()
        hlayout.setContentsMargins(2, 2, 2, 2)
        hlayout.setSpacing(2)
        hlayout.addWidget(self.about)
        hlayout.addWidget(self.min)
        hlayout.addWidget(self.max)
        hlayout.addWidget(self.restore)
        hlayout.addWidget(self.close)
        vlayout.addLayout(hlayout)
        vlayout.addStretch()
        self.hlayout.addLayout(vlayout)

        self.sigAbout = self.about.clicked
        self.setIcon(qta.icon('mdi.google-analytics',
                        color='blue',
                        color_active='orange').pixmap(self.icon.width(), self.icon.height()))
    
    def setIcon(self, icon : QtGui.QPixmap):
        self.icon.setPixmap(icon.scaled(self.icon.size()))

    def setTitle(self, title: string):
        self.title.setText(title)
    

if __name__ == "__main__" :
    from qtpy.QtWidgets import QApplication
    import os
    import sys

    app = QApplication(sys.argv)
    w = HeaderWidget()
    w.resize(1000, 800)
    w.show()
    app.exec_()