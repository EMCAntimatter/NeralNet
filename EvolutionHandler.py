import random
import threading
from time import *

import DefNode
from DefNode import inputNode
from DefNode import *
from PongGame import *


class instance():
    createdAt = time()
    fitness = 0  # edited on game over
    nodes = list(())

    selfYPos = None
    ballXPos = None
    ballYPos = None
    ballXDir = None
    ballYDir = None
    selfMoveTowardY = None

    def __init__(self, species):
        nodes = species.lastInstance.nodes

        self.selfYPos = species.lastInstance.selfYPos
        self.ballXPos = species.lastInstance.ballXPos
        self.ballYPos = species.lastInstance.ballYPos
        self.ballXDir = species.lastInstance.ballXDir
        self.ballYDir = species.lastInstance.ballYDir
        self.selfMoveTowardY = species.lastInstance.selfMoveTowardY

        self.mutateNewNode()

        for node in nodes:
            node.mutateNodeConnection()
        for node in nodes:
            node.mutateConnectionStrength()

    def mutateNewNode(self):
        if random.randrange(0, 100) <= 15:
            self.nodes.append(Node((), (), self))

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
    nodes = list(())

    def __init__(self, species):
        self.selfYPos = inputNode(list(()), list(()), self)
        self.ballXPos = inputNode(list(()), list(()), self)
        self.ballYPos = inputNode(list(()), list(()), self)
        self.ballXDir = inputNode(list(()), list(()), self)
        self.ballYDir = inputNode(list(()), list(()), self)
        self.selfMoveTowardY = outputNode(list(()), list(()), self)

        self.nodes.append(self.selfYPos)
        self.nodes.append(self.ballXPos)
        self.nodes.append(self.ballYPos)
        self.nodes.append(self.ballXDir)
        self.nodes.append(self.ballYDir)
        self.nodes.append(self.selfMoveTowardY)


class species():
    bestInstances = list(())
    lastInstance = None
    currentInstance = None
    gameInstance = None

    def fitness(self):
        self.currentInstance.fitness = time() - self.currentInstance.createdAt
        print(self.currentInstance.fitness)

    def newInstance(self):
        self.fitness()
        if self.bestInstances.__len__() > 0:
            if self.currentInstance.fitness < self.bestInstances[self.bestInstances.__len__() -1]:
                self.lastInstance = self.bestInstances[self.bestInstances.__len__() -1]
        self.lastInstance = self.currentInstance
        self.currentInstance = instance(self)
        self.gameInstance = Game(speed=4)
        if len(self.bestInstances) > 0:
            if self.lastInstance.fitness > self.bestInstances[len(self.bestInstances) - 1]:
                print("New Best Fitness: " + self.lastInstances.fitness)
                self.bestInstances.append(self.lastInstance)

    def loadInstace(self, index):
        self.fitness()
        self.lastInstance = self.currentInstance
        self.currentInstance = self.bestInstances(index)

        if self.lastInstance.fitness > self.bestInstances[len(self.bestInstances) - 1]:
            self.bestInstances.append(self.lastInstance)

    def __init__(self):
        self.lastInstance = firstInstance(self)
        self.currentInstance = instance(self)
        self.gameInstance = Game(speed=4)

    def updateIOVals(self):
        self.currentInstance.selfYPos.inputVal = self.gameInstance.paddles[0].rect.y
        self.currentInstance.ballXPos.inputVal = self.gameInstance.ball.x
        self.currentInstance.ballYPos.inputVal = self.gameInstance.ball.y
        self.currentInstance.ballXDir.inputVal = self.gameInstance.ball.dir_x
        self.currentInstance.ballYDir.inputVal = self.gameInstance.ball.dir_y
        self.currentInstance.selfMoveTowardY.createOutput()
        #print(self.currentInstance.selfMoveTowardY.outputVal)
        print(self.currentInstance.selfMoveTowardY.connections)
        self.gameInstance.userMoveTo = self.currentInstance.selfMoveTowardY.outputVal


userInput = ""
lastSpecies = 0
currentSpecies = 0

#Might want to get rid of this, could stack overflow
sys.setrecursionlimit(1000)
threading.stack_size(67108864)

while userInput != "exit":
    gens = 0
    #numGens = input("Number of generations:\n")
    numGens = 1
    numGens = int(numGens)
    # userInput = input(">>>")
    userInput = "start"  # delete after testing
    lastSpecies, currentSpecies = currentSpecies, species()
    currentSpecies.gameInstance = Game(speed=4)
    if userInput == "start":
        while gens <= numGens:
            currentSpecies.gameInstance.gameOver = False
            while not currentSpecies.gameInstance.gameOver:
                overflowPreventer = 0
                currentSpecies.newInstance()
                lastSpecies, currentSpecies = currentSpecies, species()
                main(currentSpecies.gameInstance, currentSpecies)
            ++gens
    elif userInput == "load":
        userInput = input("Enter index number or enter best")
        if userInput == "best":
            currentSpecies.loadInstace(currentSpecies.bestInstances.__len__() - 1)
        else:
            currentSpecies.loadInstace(int(userInput))
