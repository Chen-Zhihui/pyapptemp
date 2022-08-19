import logging
logging.info(f"{__file__}")
from qtpy.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel
from qtpy.QtCore import Qt
from qtpy.QtGui import QPixmap
from main.python.icons import icon_app_main
import main.python.parameters as parameters

class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

        QBtn = QDialogButtonBox.Ok  # No cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        title = QLabel(parameters.application_title)
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        layout.addWidget(title)

        logo = QLabel()
        logo.setPixmap(QPixmap(icon_app_main.pixmap(50, 50)))
        layout.addWidget(logo)

        layout.addWidget(QLabel("Version 1.0.0"))
        layout.addWidget(QLabel("Copyright 2022 SFF Inc."))

        for i in range(0, layout.count()):
            layout.itemAt(i).setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)


