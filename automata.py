from edge import Edge
from node import Node

class Automata:
    def __init__(self):

        self.LAMBDA = "$"

        self.nodesList = [
            Node("q0",50, 190,"images/q0.png","images/q0_"),
            Node("q1",150, 70,"images/q1.png","images/q1_"),
            Node("q2",510, 70,"images/q2.png","images/q2_"),
            Node("q3",270, 190,"images/q3.png","images/q3_"),
            Node("q4",150, 330,"images/q4.png","images/q4_")
            ] 

        self.edgesList = [
            #Edges of q0
            Edge("a",self.nodesList[0],self.nodesList[1],"images/q0-q1.png","images/q0-q1_",98,123,61,69),
            Edge("d",self.nodesList[0],self.nodesList[3],"images/q0-q3.png","images/q0-q3_.png",115,195,159,47),
            Edge("c",self.nodesList[0],self.nodesList[4],"images/q0-q4.png","images/q0-q4_.png",100,251,67,86),
            #Edges of q1
            Edge("a",self.nodesList[1],self.nodesList[1],"images/q1-q1.png","images/q1-q1_.png",155,26,65,66),
            Edge("b",self.nodesList[1],self.nodesList[2],"images/q1-q2.png","images/q1-q2_.png",201,24,324,67),
            Edge("d",self.nodesList[1],self.nodesList[3],"images/q1-q3.png","images/q1-q3_.png",200,130,77,80),
            Edge("c",self.nodesList[1],self.nodesList[4],"images/q1-q4.png","images/q1-q4_.png",150,135,77,200),
            #Edges of q2
            Edge("b",self.nodesList[2],self.nodesList[2],"images/q2-q2.png","images/q2-q2_.png",510,12,48,68),
            Edge("a",self.nodesList[2],self.nodesList[1],"images/q2-q1.png","images/q2-q1_.png",210,93,300,68),
            Edge("d",self.nodesList[2],self.nodesList[3],"images/q2-q3.png","images/q2-q3_.png",336,132,190,98),
            Edge("c",self.nodesList[2],self.nodesList[4],"images/q2-q4.png","images/q2-q4c.png",200,120,370,287),
            #Edges of q3
            Edge("d",self.nodesList[3],self.nodesList[3],"images/q3-q3.png","images/q3-q3_.png",300,217,72,81),
            Edge("a",self.nodesList[3],self.nodesList[2],"images/q3-q2.png","images/q3-q2_.png",329,116,191,97),
            Edge("c",self.nodesList[3],self.nodesList[4],"images/q3-q4.png","images/q3-q4_.png",195,242,95,97),
            #Edges of q4
            Edge("c",self.nodesList[4],self.nodesList[4],"images/q4-q4.png","images/q4-q4c.png",124,358,64,85),
            Edge("a",self.nodesList[4],self.nodesList[2],"images/q4-q2.png","images/q4-q2_.png",203,135,380,247),
            Edge("d",self.nodesList[4],self.nodesList[3],"images/q4-q3.png","images/q4-q3_.png",190,235,88,99)
        ]
