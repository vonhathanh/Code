import state
import copy
import queue as Q

# q = Q.PriorityQueue()
# q.put(10)
# q.put(1)
# q.put(5)
# while not q.empty():
#    print q.get()

def toTuple(data):
    return tuple(tuple(x) for x in data)

def heuristicCostEstimate(state):
    n = len(state.data)
    cost = 0
    for i in range(0, n):
        for j in range(0, n):
            if state.data[i][j] == 0:
                continue
            else:
                x = int(state.data[i][j] / n);
                y = int(state.data[i][j] % n);
                cost += abs(x - i) + abs(y - j)
    return cost


class Solver:
    Direction = ['up', 'down', 'left', 'right']
    ReverseDirection = ['right', 'left', 'down', 'up']

    # init goal state, this state is a list of list contains elements from 0 to n*n - 1
    def __init__(self, n):
        self.goal = []
        self.n = n
        for i in range(0, self.n):
            temp = []
            for j in range(i * self.n, (i + 1) * self.n):
                temp.append(j)
            self.goal.append(temp)

    # check that current state is a goal state or not
    def checkGoal(self, currentState):
        return currentState.data == self.goal

    # generate next state of current state according to direction param
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
        result = state.Result()
        frontier = []
        # create a froniter set and a visited set for O(1) time lookup
        frontierSet = set()
        visitedSet = set()
        # add first state to frontier
        frontier.append(startState)
        frontierSet.add(startState)

        while len(frontier) > 0:
            # get the first element in the frontier
            currentState = frontier[0]
            # mark this state as visited
            visitedSet.add(currentState)
            # remove it from frontier
            frontier.remove(currentState)
            frontierSet.remove(currentState)

            if self.checkGoal(currentState):
                result.state = currentState
                result.searchDepth = currentState.searchDepth
                result.fringeSize = len(frontier)
                return result

            result.nodeExpanded += 1
            for direction in self.Direction:
                nextState = self.generateNextState(currentState, direction, currentState.x, currentState.y)
                if nextState != None:
                    if nextState not in frontierSet and nextState not in visitedSet:
                        frontier.append(nextState)
                        frontierSet.add(nextState)
                        result.maxSearchDepth = max(result.maxSearchDepth, nextState.searchDepth)

            result.maxFringeSize = max(result.maxFringeSize, len(frontier))

        return None

    def DFS(self, startState):
        frontier = []
        result = state.Result()
        frontierSet = set()
        visitedSet = set()

        frontier.append(startState)
        frontierSet.add(startState)

        while len(frontier) > 0:
            currentState = frontier.pop()
            frontierSet.remove(currentState)
            visitedSet.add(currentState)

            if self.checkGoal(currentState):
                result.state = currentState
                result.searchDepth = currentState.searchDepth
                result.fringeSize = len(frontier)
                return result

            result.nodeExpanded += 1
            print(result.nodeExpanded)
            for direction in self.ReverseDirection:
                nextState = self.generateNextState(currentState, direction, currentState.x, currentState.y)
                if nextState != None:
                    if nextState not in frontierSet and nextState not in visitedSet:
                        frontier.append(nextState)
                        frontierSet.add(nextState)
                        result.maxSearchDepth = max(result.maxSearchDepth, nextState.searchDepth)

            result.maxFringeSize = max(result.maxFringeSize, len(frontier))

    def AST(self, startState):
        frontier = Q.PriorityQueue()
        frontierSet = set()
        visitedSet = set()
        result = state.Result()

        startState.gcost = 0
        startState.fcost = heuristicCostEstimate(startState)
        frontier.put(startState)
        frontierSet.add(startState)

        while not frontier.empty():
            currState = frontier.get()
            visitedSet.add(currState)
            frontierSet.remove(currState)

            if self.checkGoal(currState):
                result.state = currState
                result.searchDepth = currState.searchDepth
                result.fringeSize = frontier.qsize()
                return result

            result.nodeExpanded += 1
            for direction in self.Direction:
                nextState = self.generateNextState(currState, direction, currState.x, currState.y)
                if nextState != None:
                    if nextState in visitedSet:
                        continue
                    tentativeScore = currState.gcost + 1
                    if tentativeScore >= nextState.gcost:
                        pass



    def IDA(self, startState):
        pass
