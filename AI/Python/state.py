class State:

    def __init__(self, data, x, y, parent = None, direction = None, searchDepth = 0):
        self.data = data
        self.x = x
        self.y = y
        self.parent = parent
        self.direction = direction
        self.searchDepth = searchDepth

    def __hash__(self):
        return id(self)
    def __lt__(self, other):
        return self.data < other.data
    def __eq__(self, other):
        return self.data == other.data
    def __gt__(self, other):
        return self.data > other.data

