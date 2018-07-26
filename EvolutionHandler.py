from time import *
from Node import *
from PongGame import *

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
        self.selfYPos = inputNode(list(()), list(()), self)
        self.ballXPos = inputNode(list(()), list(()), self)
        self.ballYPos = inputNode(list(()), list(()), self)
        self.ballXVelocityRight = inputNode(list(()), list(()), self)
        self.ballXVelocityLeft = inputNode(list(()), list(()), self)
        self.ballYVelocityUp = inputNode(list(()), list(()), self)
        self.ballYVelocityDown = inputNode(list(()), list(()), self)
        self.selfMoveTowardY = outputNode(list(()), list(()), self)


class species():
    bestInstances = list(())
    lastInstance = 0
    currentInstance = 0
    gameInstance = 0

    def fitness(self):
        self.currentInstance.fitness = time() - self.currentInstance.createdAt

    def newInstance(self):
        self.fitness()
        self.lastInstance = self.currentInstance
        self.currentInstance = instance(self)
        self.gameInstance = Game(speed=4)

        if self.lastInstance.fitness > self.bestInstance[len(self.bestInstance) - 1]:
            self.bestInstances.append(self.lastInstance)

    def loadInstace(self, userInput):
        self.fitness()
        self.lastInstance = self.currentInstance
        self.currentInstance = self.bestInstances(int(userInput))

        if self.lastInstance.fitness > self.bestInstance[len(self.bestInstance) - 1]:
            self.bestInstances.append(self.lastInstance)

    def __init__(self):
        gen = 0
        numGens = input("Number of generations.")
        self.currentInstance = self.firstInstance()
        self.currentInstance.initIONodes()

        while gen <= numGens:


            if gen != 0:
                self.newInstance()
            else:
                None



            ++gen
    def updateIOVal(self):
        self.currentInstance.selfYPos = self.gameInstance.paddles['user'].rect.y
        self.currentInstance.ballXPos = self.gameInstance.ball.x
        self.currentInstance.ballYPos = self.gameInstance.ball.y
        self.currentInstance.ballXDir = self.gameInstance.ball.dir_x
        self.currentInstance.ballYDir = self.gameInstance.ball.dir_y
        self.gameInstance.userMoveTo = instance.nodes['selfMoveTowardY'].outputVal

userInput = ""
lastSpecies = 0
currentSpecies = 0



while userInput != "exit":
    userInput = input(">>>")
    if userInput == "start":
        lastSpecies, currentSpecies = currentSpecies, species()






