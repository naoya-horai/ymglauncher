import os
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
import subprocess

bat = 'bat'

class LaunchBat(qtw.QWidget):
    def __init__(self, mainwindow):
        
        super().__init__(mainwindow)

        self.layout = qtw.QVBoxLayout()

        for name in os.listdir(bat):
            button = qtw.QPushButton(name)

            button.clicked.connect(self.CallBat)

            self.layout.addWidget(button)

        self.layout.setAlignment(qtc.Qt.AlignTop)
        self.setLayout(self.layout)

    def CallBat(self):
        filename = self.sender()
        path = os.path.join(bat,filename.text())
        subprocess.run(path)
