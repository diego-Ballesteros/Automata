from node import Node 

class Edge:
    def __init__(self, character, 
            startNode, destinationNode, 
            edgeImage, edgeActiveImage,
            posx, posy,
            width,heigth
    ):
        self.character = character
        self.startNode = startNode
        self.edgeImage = edgeImage
        self.posx = posx
        self.posy = posy
        self.width = width
        self.heigth = heigth
        self.edgeActiveImage = edgeActiveImage
        self.destinationNode = destinationNode

         