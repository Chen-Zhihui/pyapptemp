from qtpy.QtWidgets import QFrame, QHBoxLayout, QSizePolicy
from .helper import zero_space
class BackWdg(QFrame):

    def __init__(self, parent) -> None:
        super(BackWdg, self).__init__()
        self.setObjectName("backWdg")
        self.layout = QHBoxLayout(self)
        # self.setStyleSheet("background-color: #2E2F30")
        zero_space(self.layout)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def addWidget(self, wdg):
        self.layout.addWidget(wdg)

