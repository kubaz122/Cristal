from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from ui import MainWindow, testDialog

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.helloWorld)

    def helloWorld(self):
        self.dialog = HelloWorld()
        self.dialog.show()


class HelloWorld(QDialog):
    def __init__(self):
        super(HelloWorld, self).__init__()
        self.ui = testDialog.Ui_Dialog()
        self.ui.setupUi(self)


app = QApplication(sys.argv)
ui = Main()
ui.show()
sys.exit(app.exec_())
