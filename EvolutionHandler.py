from time import *
from Node import *
from PongGame import *
import random

class instance():
    nodes = list(())
    createdAt = time()
    fitness = 0  # edited on game over
    def mutateNewNode(self):
        if random.randrange(0, 100) <= 15:
            self.nodes.append(Node)

    def __init__(self, species):
        if species.lastInstance != None:
            nodes = species.lastInstance.nodes
        else:
            nodes = list(())

        self.mutateNewNode()

        for node in nodes:
            node.mutateNodeConnection(node)
        for node in nodes:
            node.mutateConnectionStrength(node)

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
    lastInstance = None
    currentInstance = None
    gameInstance = None

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
        self.lastInstance = instance(self)
        gen = 0
        numGens = input("Number of generations:\n")
        numGens = int(numGens)
        self.currentInstance = firstInstance(self)
        self.currentInstance.initIONodes()

        while gen <= numGens:


            if gen != 0:
                self.newInstance()
            else:
                None



            ++gen
    def updateIOVal(self):
        self.currentInstance.selfYPos.inputVal = self.gameInstance.paddles['user'].rect.y
        self.currentInstance.ballXPos.inputVal = self.gameInstance.ball.x
        self.currentInstance.ballYPos.inputVal = self.gameInstance.ball.y
        self.currentInstance.ballXDir.inputVal = self.gameInstance.ball.dir_x
        self.currentInstance.ballYDir.inputVal = self.gameInstance.ball.dir_y
        self.gameInstance.userMoveTo.inputVal = instance.nodes['selfMoveTowardY'].outputVal

userInput = ""
lastSpecies = 0
currentSpecies = 0



while userInput != "exit":
    #userInput = input(">>>")
    userInput = "start" #delete after testing
    if userInput == "start":
        lastSpecies, currentSpecies = currentSpecies, species()
        currentSpecies.updateNodes






