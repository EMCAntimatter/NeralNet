import random

class Node():
    instance = None
    outputVal = 0
    connections = list(())
    connectionStr = list(())
    ofp = 0
    def __init__(self, connections, connectionStr, instance, ofp):
        self.ofp = ofp
        self.instance = instance
        self.instance.nodes = list(())
        index = len(self.instance.nodes)
        self.instance.nodes.append(self)
        updated = False
        connections = connections
        connectionStr = connectionStr

    def newConnection(self, node):
        if not (self.isConnectedTo(node, self.ofp) and node.isConnectedTo(self, self.ofp) and node is self and type(node) is outputNode):
            str = random.normalvariate(1, 1)

            self.connections.append(node)
            self.connectionStr.append(str)

    def isConnectedTo(self, node, ofp):
        if not (node is self) and ofp.amount <= 900:
            ofp.amount += 1
            for n in self.connections:
                if (n is node or n.isConnectedTo(node, ofp)):
                    return True
                    break

            for n in node.connections:
                if (n is self or n.isConnectedTo(self, ofp)):
                    return True
                    break
        else:
            return False

    def outputUpdateReadyQuery(self):
        for i in self.instance.nodes:
            if i.updated:
                None
            else:
                return False
                break
        return True

    def mutateNodeConnection(self):
        rand = random.randrange(0, 100)
        if rand <= 15:
            # del node
            if len(self.connections) > 1:
                i = random.randrange(0, len(self.connections) - 1)
                del self.connections[i]
                del self.connectionStr[i]
        elif rand >= 85:
            # add node
            if len(self.instance.nodes) - 1 > 1:
                i = random.randrange(0, len(self.instance.nodes) - 1)
            else:
                i = 0
            loopCounter = 0
            while not (self.isConnectedTo(self.instance.nodes[i], self.ofp)) and loopCounter <= len(self.instance.nodes) * 1.75:
                if self.instance.nodes.__len__() > 1:
                    i = random.randrange(0, self.instance.nodes.__len__() - 1)
                    break
                else:
                    loopCounter == len(self.instance.nodes) * 1.75
                    break
                loopCounter += 1
            if loopCounter != len(self.instance.nodes) * 1.75:
                self.newConnection(self.instance.nodes[i])

    def mutateConnectionStrength(self):
        for i in range(len(self.connectionStr) - 1):
            toMutate = random.normalvariate(self.connectionStr[i], .5)
            if toMutate >= 0:
                self.connectionStr[i] = toMutate
            else:
                self.connectionStr[i] = 0

    def createOutput(self):
        self.outputVal = 0
        for i in len(self.instance.nodes) - 1:
            if self.isConnectedTo(self.instance.nodes(i)):
                self.outputVal += self.instance.nodes(i).outVal * self.instance.nodes(i).connectionStr(i)

class OverflowPrevent():
    amount = 0

class inputNode(Node):
    inputVal = 0  # changed in gameloop

    def newConnection(self, node):
        None

class outputNode(Node):
    None







# test code
# node = Node((), ())
# print(node)
