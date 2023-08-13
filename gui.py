#from gui import Ui_gui
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_gui(object):
    def setupUi(self, gui):
        gui.setObjectName("gui")
        gui.resize(1059, 666)
        self.centralwidget = QtWidgets.QWidget(gui)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1061, 671))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("E:/sakshi_proj/jarvisfile/guijarvis/mic2.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(840, 620, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(47, 79, 79);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(930, 620, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(47, 79, 79);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 401, 91))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("E:/sakshi_proj/jarvisfile/guijarvis/mic3.gif"))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(590, 20, 211, 41))
        font = QtGui.QFont()

        font.setFamily("Nirmala UI")
        
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color:transparent;\n"
"border-radius:none;\n"
"color:gray;\n"
"font-size:20px;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QLabel(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(810, 20, 211, 41))
        font = QtGui.QFont()

        font.setFamily("Nirmala UI")
        
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("background-color:transparent;\n"
"border-radius:none;\n"
"color:gray;\n"
"font-size:20px;")
        
        self.textBrowser_2.setObjectName("textBrowser_2")
        gui.setCentralWidget(self.centralwidget)

        self.retranslateUi(gui)
        QtCore.QMetaObject.connectSlotsByName(gui)

    def retranslateUi(self, gui):
        _translate = QtCore.QCoreApplication.translate
        gui.setWindowTitle(_translate("gui", "MainWindow"))
        self.pushButton.setText(_translate("gui", "Run"))
        self.pushButton_2.setText(_translate("gui", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gui = QtWidgets.QMainWindow()
    ui = Ui_gui()
    ui.setupUi(gui)
    gui.show()
    sys.exit(app.exec_())
