from operator import index
from qtpy.QtWidgets import (
    QFrame,
    QLineEdit, 
    QPushButton, 
    QLabel, 
    QHBoxLayout,
    QFileDialog
    )

from qtpy.QtCore import (
    Qt, 
    Signal
)

import os.path 

from main.python.widget import zero_space, plain_frame, todo


class FileSelector(QFrame):

    sigFilePathChanged = Signal(str)

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.caption = "" 
        self.filter = "任意文件(*.*)"
        self._init_layout()
        self._init_actions()

    def _init_layout(self):
        plain_frame(self)
        self.layout = QHBoxLayout(self)
        self.layout.addStretch()
        self.title = QLabel(self)
        self._filepath = QLineEdit(self)
        self._filepath.setReadOnly(True)
        self._filepath.setMinimumWidth(300)
        self.btn = QPushButton(self)
        self.btn.setMinimumHeight(30)
        self.btn.setMinimumWidth(100)

        for w in [self.title, self._filepath, self.btn]:
            self.layout.addWidget(w)
        
    def _init_actions(self):
        self.btn.pressed.connect(self.on_to_change_path)

    def accept_file(self, filepath):
        if os.path.normpath(filepath) == os.path.normpath(self._filepath.text()):
            return 
        self._filepath.setText(os.path.normpath(filepath))
        self.sigFilePathChanged.emit(os.path.normpath(filepath))

    def get_file(self):
        return self._filepath.text()

    def set_path(self, path):
        self._filepath.setText(os.path.normpath(path))

    def setup(self, btnname, filepath, title, caption, filter):
        self._filepath.setText(filepath)
        self.title.setText(title)      
        self.btn.setText(btnname)  
        self.caption = caption 
        self.filter = filter

    def on_to_change_path(self):
        todo("Add New Class")

        
class NewFileSelector(FileSelector):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
       
    def on_to_change_path(self):
        dest, _ = QFileDialog.getSaveFileName(
            caption=self.caption,
            filter=(self.filter)
            )
        if _ :            
            self.accept_file(dest)
        
class ExistFileSelector(FileSelector):
    def __init__(self, parent=None) -> None:
        super(ExistFileSelector, self).__init__(parent)

    def on_to_change_path(self):
        path, _ = QFileDialog.getOpenFileName(
            caption = self.caption,
            filter= self.filter
        )
        if _ and os.path.exists(os.path.normpath(path)):
            self.accept_file(path)

class ExistDirSelector(FileSelector):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

    def on_to_change_path(self):
        path = QFileDialog.getExistingDirectory(
            self,
            caption = self.caption,
            directory = os.path.curdir
        )
        if os.path.exists(os.path.normpath(path)):
            self.accept_file(path)


def save_df_to_csv(df):    
    dest, _ = QFileDialog.getSaveFileName(
        caption="保存CSV文件",
        filter="CSV文件(*.csv)"
        )
    if _ :            
        df.to_csv(dest, index=False)
        return dest
    else:
        return None