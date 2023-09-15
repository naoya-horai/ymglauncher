import os
from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc

class CreateBat(qtw.QWidget):
    def __init__(self,mainwindow):
        super().__init__(mainwindow)

        self.layout = qtw.QVBoxLayout()
        self.envStrList = []
        
        self.exeWidget = qtw.QWidget(self)
        self.exeLayout = qtw.QHBoxLayout(self.exeWidget)
        self.exePath = qtw.QLineEdit("", self.exeWidget)
        self.exeButton = qtw.QPushButton("file", self.exeWidget)
        self.exeLayout.addWidget(self.exePath)
        self.exeLayout.addWidget(self.exeButton)

        self.envWidget = qtw.QWidget(self)
        self.envLayout = qtw.QHBoxLayout(self.envWidget)
        self.envAddButton = qtw.QPushButton("add val", self.envWidget)
        self.envDelButton = qtw.QPushButton("del val", self.envWidget)
        self.envLayout.addWidget(self.envAddButton)
        self.envLayout.addWidget(self.envDelButton)

        self.EShelfArea = qtw.QScrollArea(self)
        self.EShelfArea.setWidgetResizable(True)
        self.EShelfWidget = qtw.QWidget(self)
        self.EShelfLayout = qtw.QVBoxLayout(self.EShelfWidget)
        self.EShelfLayout.setAlignment(qtc.Qt.AlignTop)
        self.EShelfArea.setWidget(self.EShelfWidget)
        
        self.exportWidget = qtw.QWidget(self)
        self.exportLayout = qtw.QHBoxLayout(self.exportWidget)
        self.exportName = qtw.QLineEdit("", self.exportWidget)
        self.exportButton = qtw.QPushButton("Export", self.exportWidget)
        self.exportLayout.addWidget(self.exportName)
        self.exportLayout.addWidget(self.exportButton)
        
        self.layout.addWidget(self.exeWidget)
        self.layout.addWidget(self.envWidget)
        self.layout.addWidget(self.EShelfArea)
        self.layout.addWidget(self.exportWidget)

        self.setLayout(self.layout)
        self.exeButton.clicked.connect(self.showDialog)
        self.envAddButton.clicked.connect(self.addEnvBox)
        self.envDelButton.clicked.connect(self.delEnvBox)
        self.exportButton.clicked.connect(self.batcreate)

        
    
    def showDialog(self):
            options = qtw.QFileDialog.Options()
            exepath = qtw.QFileDialog.getOpenFileName(self, "exeを選択", "", options=options)
            
            if exepath:
                self.exePath.setText(exepath[0])
                print("Selected folder:", exepath[0])
    
    def addEnvBox(self):
        count = self.EShelfLayout.count()
        groupBox = qtw.QGroupBox("env" + str(count), self.EShelfWidget)
        self.EShelfLayout.insertWidget(count, groupBox)

        envStr = qtw.QLineEdit(groupBox)

        layout = qtw.QVBoxLayout(groupBox)
        layout.addWidget(envStr)
    
    def delEnvBox(self):
        count = self.EShelfLayout.count()
        if count == 0:
              return
        
        item = self.EShelfLayout.itemAt(count - 1)
        widget = item.widget()
        widget.deleteLater()

    def batcreate(self):
        if self.exePath.text():
            path = './bat/'
            path = os.path.join(path,self.exportName.text()+'.bat')
            f = open(path, 'w')
            count = self.EShelfLayout.count()
            print(count)
            if count == 0:
                pass
            else:
                 for i in range(count):
                    f.write(self.EShelfLayout.itemAt(i).widget().layout().itemAt(0).widget().text() + "\n")
                    
                        
            f.write(r'start "" "{}"'.format(self.exePath.text()))
            f.close()