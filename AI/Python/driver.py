import sys
from state import *
from solver import *
import math


def main(argv):
    args = [1, 2, 5, 3, 4, 0, 6, 7, 8]
    startState = []
    n = int(math.sqrt(len(args)))
    x = -1
    y = -1
    for i in range(0, n):
        startState.append(args[i * n: (i + 1) * n])
    for i in range(0, n):
        for j in range(0, n):
            if startState[i][j] == 0:
                x = i
                y = j
                break
    if x != -1 and y != -1:
        state = State(startState, x, y)
        solver = Solver(n)
        result, fringeSize, maxFringeSize, nodeExpanded, searchDepth, maxSearchdepth = solver.BFS(state)
        cost = 0
        print "path to goal: "
        while result.parent != None:
            cost += 1
            print result.direction
            result = result.parent
        print "cost of path: ", cost
        print "fringe size: ", fringeSize
        print "max fringe size: ", maxFringeSize
        print "node expanded: ", nodeExpanded
        print "search depth: ", searchDepth
        print "max search depth: ", maxSearchdepth
    else:
        print "the input is invalid"
        # state = State(startState)
        # solver = Solver()
        # solver.BFS(state)


main(sys.argv)
