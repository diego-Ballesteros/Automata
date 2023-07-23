from PySide6.QtWidgets import QApplication
from mainwindow import Ui_MainWindow
import sys

class Launcher( Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Launcher()
    window.show()
    sys.exit(app.exec_())