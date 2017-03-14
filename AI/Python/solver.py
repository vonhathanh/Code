import state


class Solver:
    Direction = ['up', 'down', 'left', 'right']

    def __init__(self, n):
        self.goal = []
        self.n = n
        for i in range(0, self.n):
            temp = []
            for j in range(i, (i + 1) * self.n):
                temp.append(j)
            self.goal.append(temp)

    def checkGoal(self, currentState):
        for i in range(0, self.n):
            for j in range(0, self.n):
                if currentState.data[i][j] != self.goal[i][j]:
                    return False
        return True

    def generateNextState(self, currentState, direction, x, y):
        if direction == 'up':
            if x == 0:
                return None
            nextState = currentState
            nextState[x][y] = currentState[x - 1][y]
            nextState[x - 1][y] = 0
            return state.State(nextState, x - 1, y)
        elif direction == 'down':
            if x == self.n - 1:
                return None
            nextState = currentState
            nextState[x][y] = currentState[x + 1][y]
            nextState[x + 1][y] = 0
            return state.State(nextState, x + 1, y)
        elif direction == 'left':
            if y == 0:
                return None
            nextState = currentState
            nextState[x][y] = currentState[x][y - 1]
            nextState[x][y - 1] = 0
            return state.State(nextState, x, y - 1)
        elif direction == 'right':
            if y == self.n - 1:
                return None
            nextState = currentState
            nextState[x][y] = currentState[x][y + 1]
            nextState[x][y + 1] = 0
            return state.State(nextState, x, y + 1)

    def BFS(self, startState):
        frontier = []
        visited = set()
        frontier.append(startState)
        # visited.add(startState)
        while len(frontier) > 0:
            currentState = frontier[0]
            visited.add(currentState)
            frontier.remove(currentState)
            if self.checkGoal(currentState):
                return currentState
            for direction in self.Direction:
                nextState = self.generateNextState(currentState.data, direction, currentState.x, currentState.y)
                if nextState != None:
                    if nextState not in visited and nextState not in frontier:
                        frontier.append(nextState)
        return None

    def DFS(self, startState):
        pass

    def AST(self, startState):
        pass

    def IDA(self, startState):
        pass
