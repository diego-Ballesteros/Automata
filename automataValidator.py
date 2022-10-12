from automata import Automata
from node import Node
from automataListener import AutomataListener


class AutomataValidator:    

    def __init__(self, automata : Automata, inputString,automataListener : AutomataListener):
        self.inputString = inputString
        self.automata = automata
        self.IteratorInputString = 0
        self.automataListener = automataListener
        self.edgeFinderPos = 0

    def isInputStringValidate(self):
        if self.inputString[0] == self.automata.LAMBDA:
            if len(self.inputString) == 1:
                self.automataListener.automataTracked(f'\nLlego a "{self.automata.nodesList[0].id}"')
                self.automataListener.nodeValidated(0)           
                return True
                      
            else: return False
        iteratorNode = self.automata.nodesList[0]
        self.automataListener.automataTracked(f'\nLlego a "{self.automata.nodesList[0].id}"')
        self.automataListener.nodeValidated(0)
        for charInputString in self.inputString:
            findedEdge = self.findEdge(iteratorNode,charInputString)
            if findedEdge == None:
                return False
            else:
                self.automataListener.automataTracked(f'\nDesde "{iteratorNode.id}"  pasando por la arista "{findedEdge.character}" con destino a "{findedEdge.destinationNode.id}"')
                self.automataListener.edgeValidated(self.edgeFinderPos)
                iteratorNode = findedEdge.destinationNode
                self.automataListener.automataTracked(f'\nLlego a "{iteratorNode.id}"')
                self.automataListener.nodeValidated(self.findNodePos(iteratorNode))
                
                
        return True
        
    

    def findEdge(self, currentNode: Node, character):
        self.edgeFinderPos = 0
        for edge in self.automata.edgesList:
            if edge.character == character and currentNode == edge.startNode:
                return edge
            self.edgeFinderPos +=1
        return None

    def findNodePos(self, currentNode: Node):
        nodeFinderPos = 0
        for node in self.automata.nodesList:
            if currentNode == node:
                return nodeFinderPos
            nodeFinderPos +=1
        return None