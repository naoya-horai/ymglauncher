import sys
import os

from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg
from PySide6 import QtWidgets as qtw

import launchbat
import createbat

class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("ymglauncher")
        self.setGeometry(0,0,480,480)
        
        self.MainWidget = qtw.QWidget(self)
        self.MainLayout = qtw.QHBoxLayout(self.MainWidget)

        self.separator = qtw.QFrame(self.MainWidget)
        self.separator.setFrameShape(qtw.QFrame.VLine)
        self.separator.setFrameShadow(qtw.QFrame.Sunken)

        self.SideBarWidget = qtw.QWidget(self.MainWidget)
        self.SideBarLayout = qtw.QVBoxLayout(self.SideBarWidget)
        self.LaunchButton = qtw.QPushButton("launch", self.SideBarWidget)
        self.CreateButton = qtw.QPushButton("Create", self.SideBarWidget)
        self.SideBarLayout.addWidget(self.LaunchButton)
        self.SideBarLayout.addWidget(self.CreateButton)
        self.SideBarLayout.setAlignment(qtc.Qt.AlignTop)

        self.MainLayout.addWidget(self.SideBarWidget)
        self.MainLayout.addWidget(self.separator)
        self.MainLayout.addWidget(launchbat.LaunchBat(self))

        self.SideBarWidget.setFixedWidth(100)

        

        self.setCentralWidget(self.MainWidget)

        self.show()

        self.LaunchButton.clicked.connect(self.launchWidget)
        self.CreateButton.clicked.connect(self.createWidget)


    def launchWidget(self):
        count = self.MainLayout.count()
        if count == 0:
              return
        
        item = self.MainLayout.itemAt(count - 1)
        widget = item.widget()
        widget.deleteLater()
        widget = launchbat.LaunchBat(self)
        self.MainLayout.addWidget(widget)
    
    def createWidget(self):
        count = self.MainLayout.count()
        if count == 0:
              return
        
        item = self.MainLayout.itemAt(count - 1)
        widget = item.widget()
        widget.deleteLater()
        widget = createbat.CreateBat(self)
        self.MainLayout.addWidget(widget)
    



if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    app.setStyleSheet("""
    QMainWindow {
        background-color: #333;
    }
    QPushButton {
        background-color: #555;
        color: white;
    }
    """)
    mw = MainWindow()
    sys.exit(app.exec())