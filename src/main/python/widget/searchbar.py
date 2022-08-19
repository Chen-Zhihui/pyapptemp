from qtpy.QtWidgets import (
    QLineEdit, 
    QToolButton,
    QToolBar,
    QHBoxLayout,
    QFrame,
    QSizePolicy,
    QAction
)
from qtpy.QtCore import (
    Qt, 
    Signal,
    QSortFilterProxyModel
)
import qtawesome as qta
from main.python.widget.helper import zero_space

class SearchBar(QToolBar):

    valueChanged = Signal(str)

    def __init__(self, parent) -> None:
        super(QToolBar, self).__init__(parent)
        self._init_layout()
        self._init_actions()

    def _init_layout(self):
        # self.layout = QHBoxLayout(self)
        # zero_space(self.layout)
        self.editor = QLineEdit(self)
        self.clear = QAction(
            qta.icon("fa5b.searchengin",
                        color='blue',
                        color_active='orange',
                        opacity=0.7), 
            "清除",
            triggered=lambda _: self.editor.setText("")
        )
        self.addWidget(self.editor)
        self.addAction(self.clear)


    def _init_actions(self):
        self.editor.textChanged.connect(lambda _ : self.valueChanged.emit(_))

    
class SortFilterModel(QSortFilterProxyModel):
    pass
