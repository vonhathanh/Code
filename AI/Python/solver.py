import state
import copy

class Solver:
    Direction = ['up', 'down', 'left', 'right']
    ReverseDirection = ['right', 'left', 'down', 'up']

    def __init__(self, n):
        self.goal = []
        self.n = n
        for i in range(0, self.n):
            temp = []
            for j in range(i * self.n, (i + 1) * self.n):
                temp.append(j)
            self.goal.append(temp)

    def checkGoal(self, currentState):
        return currentState.data == self.goal

    def generateNextState(self, currentState, direction, x, y):
        if direction == 'up':
            if x == 0:
                return None
            nextState = copy.deepcopy(currentState.data)
            nextState[x][y] = nextState[x - 1][y]
            nextState[x - 1][y] = 0
            return state.State(nextState, x - 1, y, currentState, direction, currentState.searchDepth + 1)
        elif direction == 'down':
            if x == self.n - 1:
                return None
            nextState = copy.deepcopy(currentState.data)
            nextState[x][y] = nextState[x + 1][y]
            nextState[x + 1][y] = 0
            return state.State(nextState, x + 1, y, currentState, direction, currentState.searchDepth + 1)
        elif direction == 'left':
            if y == 0:
                return None
            nextState = copy.deepcopy(currentState.data)
            nextState[x][y] = nextState[x][y - 1]
            nextState[x][y - 1] = 0
            return state.State(nextState, x, y - 1, currentState, direction, currentState.searchDepth + 1)
        elif direction == 'right':
            if y == self.n - 1:
                return None
            nextState = copy.deepcopy(currentState.data)
            nextState[x][y] = nextState[x][y + 1]
            nextState[x][y + 1] = 0
            return state.State(nextState, x, y + 1, currentState, direction, currentState.searchDepth + 1)

    def BFS(self, startState):
        maxFringeSize = 0
        maxSearchDepth = 0
        nodeExpanded = 0
        frontier = []
        visited = []
        frontier.append(startState)
        while len(frontier) > 0:
            currentState = frontier[0]
            visited.append(currentState)
            frontier.remove(currentState)
            if self.checkGoal(currentState):
                return currentState, \
                       len(frontier), \
                       maxFringeSize, \
                       nodeExpanded, \
                       currentState.searchDepth, \
                       maxSearchDepth
            for direction in self.Direction:
                nextState = self.generateNextState(currentState, direction, currentState.x, currentState.y)
                if nextState != None:
                    if nextState not in frontier and nextState not in visited:
                        nodeExpanded += 1
                        frontier.append(nextState)
                        maxSearchDepth = max(maxSearchDepth, nextState.searchDepth)

            maxFringeSize = max(maxFringeSize, len(frontier))

        return None

    def DFS(self, startState):
        maxFringeSize = 0
        maxSearchDepth = 0
        nodeExpanded = 0
        frontier = []
        visited = []
        frontierSet = set()
        visitedSet = set()

        frontier.append(startState)
        frontierSet.add(startState)
        while len(frontier) > 0:
            currentState = frontier.pop()
            frontierSet.remove(currentState)
            # print currentState.data[0], "\n", currentState.data[1], "\n", currentState.data[2], "\n"
            visited.append(currentState)
            visitedSet.add(currentState)
            if self.checkGoal(currentState):
                return currentState, \
                       len(frontier), \
                       maxFringeSize, \
                       nodeExpanded, \
                       currentState.searchDepth, \
                       maxSearchDepth
            nodeExpanded += 1
            print nodeExpanded
            for direction in self.ReverseDirection:
                nextState = self.generateNextState(currentState, direction, currentState.x, currentState.y)
                if nextState != None:
                    if nextState not in frontierSet and nextState not in visitedSet:
                        frontier.append(nextState)
                        frontierSet.add(nextState)
                        maxSearchDepth = max(maxSearchDepth, nextState.searchDepth)
            maxFringeSize = max(maxFringeSize, len(frontier))

    def AST(self, startState):
        pass

    def IDA(self, startState):
        pass
