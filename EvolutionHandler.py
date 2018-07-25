from time import *
from Node import *

class instance():
    nodes = list(())
    createdAt = time()
    fitness = 0  # edited on game over

    def mutateNewNode(self):
        if random(0, 100) <= 15:
            self.nodes[len(self.nodes)] = Node

    def __init__(self, species):

        nodes = species.lastInstance.nodes

        self.mutateNewNode()

        for node in nodes:
            node.mutateNodeConnection()
        for node in nodes:
            node.mutateConnectionStrength()

    def allNodesUTD(self):
        for i in self.nodes:
            if not i.updated:
                return False
                break
        return True

    def updateNodes(self):
        while not self.allNodesUTD():
            for i in self.nodes:
                if i.outputUpdateReadyQuery:
                    i.createOutput()
                else:
                    None


class firstInstance(instance):
    # Input and output names and amounts must be manually edited for now
    selfYPos = None
    ballXPos = None
    ballYPos = None
    ballXVelocityRight = None
    ballXVelocityLeft = None
    ballYVelocityUp = None
    ballYVelocityDown = None
    selfMoveTowardY = None

    def initIONodes(self):
        selfYPos = inputNode(list(()), list(()), self)
        ballXPos = inputNode(list(()), list(()), self)
        ballYPos = inputNode(list(()), list(()), self)
        ballXVelocityRight = inputNode(list(()), list(()), self)
        ballXVelocityLeft = inputNode(list(()), list(()), self)
        ballYVelocityUp = inputNode(list(()), list(()), self)
        ballYVelocityDown = inputNode(list(()), list(()), self)
        selfMoveTowardY = outputNode(list(()), list(()), self)


class species():
    bestInstances = list(())
    lastInstance = 0
    currentInstance = 0

    def fitness(self):
        self.currentInstance.fitness = time() - self.currentInstance.createdAt

    def newInstance(self):
        self.fitness()
        self.lastInstance = self.currentInstance
        self.currentInstance = instance(self)

        if self.lastInstance.fitness > self.bestInstance[len(self.bestInstance) - 1]:
            self.bestInstances.append(self.lastInstance)

    def loadInstace(self, userInput):
        self.fitness()
        self.lastInstance = self.currentInstance
        self.currentInstance = self.bestInstances(int(userInput))

        if self.lastInstance.fitness > self.bestInstance[len(self.bestInstance) - 1]:
            self.bestInstances.append(self.lastInstance)

def runSpecies():
    numGens = input("Number of generations.")
    spec = species()
    for x in numGens:
        spec.newInstance()
        inst = spec.currentInstance

# MAIN
userInput = ""

while userInput != "exit":
    userInput = input(">>>")
    if userInput == "start":
        runSpecies()






