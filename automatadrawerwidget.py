from turtle import pos
from automata import Automata
from automatawidget import AutomataWidget
from edge import Edge
from nodewidget import NodeWidget
from edgewidget import EdgeWidget
from PySide6.QtCore import QRect
from automataListener import AutomataListener
from PySide6.QtWidgets import QLabel


class AutomataDrawer(AutomataListener):
    def __init__(self,autamata: Automata, automataWidget : AutomataWidget, trackLabel : QLabel, time : int):
        self.automata = autamata
        self.automataWidget = automataWidget
        self.nodeWidgetList = []
        self.edgeWidgetList = []
        self.trackLabel = trackLabel
        self.time = time

    def setTime(self, time):
        self.time = time

    def drawAutomata(self):
        self.drawEdges()
        self.drawNodes()

    def resetAutomata(self):
        self.resetEdge()
        self.resetNode()

    def drawNodes(self):
        for node in self.automata.nodesList:
            nodeWidget = NodeWidget(node,self.automataWidget)
            nodeWidget.setGeometry(QRect(node.posx, node.posy, nodeWidget.BUFFER_SIZE, nodeWidget.BUFFER_SIZE))
            nodeWidget.showNode()
            self.nodeWidgetList.append(nodeWidget)            
        
    def drawEdges(self):
        for edge in self.automata.edgesList:
            edgeWidget = EdgeWidget(edge,self.automataWidget)
            edgeWidget.setGeometry(QRect(edge.posx, edge.posy, edge.width, edge.heigth))
            edgeWidget.showEdge()
            self.edgeWidgetList.append(edgeWidget)

    def resetEdge(self):
        for edgeWidget in self.edgeWidgetList:
            edgeWidget.showEdge()
        
    def resetNode(self):
        for nodeWidget in self.nodeWidgetList:
            nodeWidget.showNode()     
            
    def activeEdge(self, pos):
        self.edgeWidgetList[pos].showEdgeActiveAnimation(self.time)

    def activeNode(self, pos):
        self.nodeWidgetList[pos].showNodeActiveAnimation(self.time)
        
    def nodeValidated(self, pos):
        self.activeNode(pos)

    def edgeValidated(self, pos):
        self.activeEdge(pos)       

    def automataTracked(self,text):
        self.trackLabel.setText(text)
    
