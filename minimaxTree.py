from library import utilityFunction
import copy
import gym
from gym_chess import ChessEnvV1, ChessEnvV2

class minimaxTree:
    def __init__(self, state, maxDepth):
        self.headNode = node(state, 0)
        self.maxDepth = maxDepth

    def generateTree(self, currentNode, depth):
        if depth < self.maxDepth:
            print(str(depth) + "**************************************************************************************************************************8")
            currentNode.generateChildren("black" if depth % 2 == 0 else "white")
            for child in currentNode.children:
                self.generateTree(child, depth + 1)

    def render(self, cNode):
        if(cNode):
            print(cNode.action)
            for child in cNode.children:
                self.render(child)
            
class node:
    def __init__(self, state, action):
        self.state = state
        self.action = action
        self.minimaxValue = 0
        self.children = []
    
    def generateChildren(self, move):
        if move == "black":
            workingEnv = ChessEnvV2(initial_board=self.state["board"], opponent=nullmove, player_color="BLACK")
        else:
            workingEnv = ChessEnvV2(initial_board=self.state["board"], opponent="none")
        possibleActions = workingEnv.possible_actions
        for action in possibleActions:
            new_state, reward, done, info = workingEnv.step(action)
            chNode = node(new_state, action)
            self.children.append(chNode)
            workingEnv.reset()
            
def nullmove(env):
    board = env.state["board"]
    for rowInd in range(len(board)):
        for colInd in range(len(board[0])):
            if board[rowInd][colInd] == 1 or board[rowInd][colInd] == -1:
                return ((rowInd,colInd), (rowInd,colInd))
        
    