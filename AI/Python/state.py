import solver
import sys

class State:
    def __init__(self, data, x, y, parent=None, direction=None, searchDepth=0):
        self.data = data
        self.x = x
        self.y = y
        self.parent = parent
        self.direction = direction
        self.searchDepth = searchDepth


    def __hash__(self):
        return hash(solver.toTuple(self.data))

    def __lt__(self, other):
        return self.data < other.data

    def __eq__(self, other):
        return self.data == other.data

    def __gt__(self, other):
        return self.data > other.data

class ASState(State):
    def __init__(self, data, x, y, parent=None, direction=None, searchDepth=0):
        super(ASState,self).__init__(data,x,y,parent,direction,searchDepth)
        self.fcost = sys.maxsize
        self.gcost = sys.maxsize

    def __lt__(self, other):
        return self.fcost < other.fcost

    def __eq__(self, other):
        return self.fcost == other.fcost

    def __gt__(self, other):
        return self.fcost > other.fcost

class Result:
    def __init__(self):
        self.state = None
        self.pathToGoal = []
        self.costOfPath = 0
        self.nodeExpanded = 0
        self.fringeSize = 0
        self.maxFringeSize = 0
        self.searchDepth = 0
        self.maxSearchDepth = 0
        self.runningTime = 0.0
        self.maxRamusage = 0.0
