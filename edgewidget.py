from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap
from PySide6 import QtTest
from edge import Edge
from helpers import absPath

class EdgeWidget(QLabel):
    def __init__(self, edge : Edge,parent = None):
        super().__init__(parent)
        self.edge = edge

    def showEdge(self):
        self.pixmap = QPixmap(absPath(self.edge.edgeImage))
        self.setPixmap(self.pixmap)
        self.visible = True
        
    def showEdgeActiveAnimation(self, time):
        self.pixmap = QPixmap(absPath(self.edge.edgeActiveImage))
        self.setPixmap(self.pixmap)
        self.visible = True
        QtTest.QTest.qWait(time)

        
        