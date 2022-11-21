from library import utilityFunction
import copy
import gym
import random
from gym_chess import ChessEnvV1, ChessEnvV2

class minimaxTree:
    def __init__(self, state, maxDepth):
        self.headNode = node(state, 0)
        self.maxDepth = maxDepth

    #this function generates the tree with the depth that corolates to the different difficulties 
    def generateTree(self, currentNode, depth):
        if depth < self.maxDepth:
            currentNode.generateChildren("black" if depth % 2 == 0 else "white")
            for child in currentNode.children:
                self.generateTree(child, depth + 1)

    #This is the function that runs the minimax algorithm on the generated tree 
    def runMiniMaxAlgorithm(self):
        #first run the utility algorithm on the bottom row
        self.runUtilityAlgorithm(self.headNode, self.maxDepth - 1)
        
        #Then preform the bring up algorithm 
        for i in range(self.maxDepth - 1):
            fIndex = (self.maxDepth - 2) - i
            self.traverseLevel(self.headNode, fIndex, "max" if fIndex % 2 == 0 else "min")
        
        # print("Starting Print*******************************************88")
        # self.printLevel(self.headNode, 2)
        # print("level 1 ********************************************************88")
        # self.printLevel(self.headNode, 1)
        # print("level 0 ********************************************************88")
        # self.printLevel(self.headNode, 0)

    def returnBestMove(self, env):
        bestMoveIndex = self.headNode.bestMove
        return env.action_to_move(self.headNode.children[bestMoveIndex].action)
        
    #This function traverses through the tree and if at the specified depth preforms the minimax algorithm  
    def printLevel(self, currentNode, level):
        if currentNode is None:
            return
        if level == 0:
            #run algorithm
            print(currentNode.minimaxValue)              
            return
        elif level > 0:
            for child in currentNode.children:
                self.printLevel(child, level - 1)

    def traverseLevel(self, currentNode, level, mimx):
        if currentNode is None:
            return
        if level == 0:
            #run algorithm
            if mimx == "max":
                currentNode.minimaxValue, currentNode.bestMove = max(currentNode.children)
            else:
                currentNode.minimaxValue, currentNode.bestMove = min(currentNode.children)         
            return
        elif level > 0:
            for child in currentNode.children:
                self.traverseLevel(child, level - 1, mimx)
    
    def runUtilityAlgorithm(self, currentNode, level):
        if currentNode is None:
            return
        if level == 0:
            #run algorithm
            currentNode.minimaxValue = utilityFunction(currentNode.state)
            return
        elif level > 0:
            for child in currentNode.children:
                self.runUtilityAlgorithm(child, level - 1)
        

    #this function is just for testing
    def render(self, cNode):
        if(cNode):
            print(cNode.action)
            for child in cNode.children:
                self.render(child)
            
class node:
    def __init__(self, state, action):
        self.state = state
        self.action = action
        self.minimaxValue = -999
        self.bestMove = -999
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

def max(children):
    maxVal = -100
    bestMoves = []

    for i in range(len(children)):
        if children[i].minimaxValue > maxVal:
            maxVal = children[i].minimaxValue
            bestMoves = [i]
        elif children[i].minimaxValue == maxVal:
            bestMoves.append(i)

    return maxVal, random.choice(bestMoves)
    

def min(children):
    minVal = 100
    bestMoves = []

    for i in range(len(children)):
        if children[i].minimaxValue < minVal:
            minVal = children[i].minimaxValue
            bestMoves = [i]
        elif children[i].minimaxValue == minVal:
            bestMoves.append(i)

    return minVal, random.choice(bestMoves)
