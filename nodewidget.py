from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QColor, QFont, QPixmap
from PySide6.QtCore import Qt
from PySide6 import QtTest
from node import Node
from helpers import absPath

class NodeWidget(QLabel):
    def __init__(self, node: Node, parent = None):
        super().__init__(parent)
        self.node = node
        self.CIRCLE_SIZE = 60
        self.BUFFER_SIZE = 70

    def drawNode(self, event):
        self.qp.setPen(QColor(0,0,0))
        self.qp.setFont(QFont("Consolas",20))
        self.qp.drawText(event.rect(),Qt.AlignCenter, self.node.id)

    def showNode(self):
        self.pixmap = QPixmap(absPath(self.node.nodeImage))
        self.setPixmap(self.pixmap)
        self.visible = True

    def showNodeActiveAnimation(self, time):
        self.pixmap = QPixmap(absPath(self.node.nodeActiveImage))
        self.setPixmap(self.pixmap)
        self.visible = True
        QtTest.QTest.qWait(time)