class Node:
    def __init__(self, id, posx, posy, nodeImage, nodeActiveImage):
        self.id = id
        self.posx = posx
        self.posy = posy
        self.nodeImage = nodeImage
        self.nodeActiveImage = nodeActiveImage
        self.isAccepted = True