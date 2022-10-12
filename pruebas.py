from PySide6 import QtGui
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPainter, QBrush, QPen
from PySide6.QtCore import Qt
import sys

class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Drawing Tutorial"
        self.top= 150
        self.left= 150
        self.width = 500
        self.height = 500
        self.InitWindow()
    
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def paintEvent(self,event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.green,  8, Qt.DashLine))
        painter.drawEllipse(40, 40, 400, 400)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
