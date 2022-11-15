from library import utilityFunction

class node:
    def __init__(self, boardState, move, value):
        self.utilValue = utilityFunction(boardState)
        self.move = move
        self.value = value