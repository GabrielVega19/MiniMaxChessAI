from library import utilityFunction
import copy
import gym
import random
from gym_chess import ChessEnvV1, ChessEnvV2

#this class handles all the minimax algorithm related calculations and it stores the head node for the tree and the max depth for the tree
class minimaxTree:
    def __init__(self, state, maxDepth):
        self.headNode = node(state, 0)
        self.maxDepth = maxDepth

    #this is a recursive function generates the tree with the depth that is decided by ai difficulty, need to run first
    def generateTree(self, currentNode, depth):
        if depth < self.maxDepth:
            #this is a helper function assosiated with the nodes that generate all the children(one for each possible move at the current board state)
            currentNode.generateChildren("black" if depth % 2 == 0 else "white")
            for child in currentNode.children:
                self.generateTree(child, depth + 1)

    #This is the function that runs the minimax algorithm on the generated tree, need to run second 
    def runMiniMaxAlgorithm(self):
        #first runs the utility algorithm on the bottom row of the tree(uses a level order traversal to acomplish)
        self.runUtilityAlgorithm(self.headNode, self.maxDepth - 1)
        
        #Then preform the algorithm to bring up the minimax values on every row besides the bottom row of the tree(loops through all the levels and then uses a level order traversal to acomplish)
        for i in range(self.maxDepth - 1):
            #flips the index so it runs bottom to top not the other way around
            fIndex = (self.maxDepth - 2) - i
            self.traverseLevel(self.headNode, fIndex, "max" if fIndex % 2 == 0 else "min")

    #after the tree is generated and you have run the algorithm you can call this function to return the generated best move from the tree and if there
    #is multiple children with the same minimax value then it choses one of them randomly 
    def returnBestMove(self, env):
        minimaxVal = self.headNode.minimaxValue
        bestActions = []

        for child in self.headNode.children:
            if child.minimaxValue == minimaxVal:
                bestActions.append(child.action)

        return env.action_to_move(random.choice(bestActions))
        
    #this is used for debugging to print out the minimax values at a certain level in the tree (uses level order traversal with recursion)
    def printLevel(self, currentNode, level):
        if currentNode is None:
            return
        if level == 0:
            #if at the desired level print out the minimax value
            print(currentNode.minimaxValue)              
            return
        elif level > 0:
            for child in currentNode.children:
                self.printLevel(child, level - 1)

    #This function traverses through the tree recursively and if at the specified level then looks at its children and brings up either the min or max value(uses level order traversal)
    def traverseLevel(self, currentNode, level, mimx):
        if currentNode is None:
            return
        if level == 0:
            #if at the desired level it looks through children and the brings up the minimax value
            if mimx == "max":
                currentNode.minimaxValue = max(currentNode.children)
            else:
                currentNode.minimaxValue = min(currentNode.children)         
            return
        elif level > 0:
            for child in currentNode.children:
                self.traverseLevel(child, level - 1, mimx)
    
    #This function traverses through the tree recursively and if at the specified level then it runs the utility function on that level(uses level order traversal)
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
            
#this class holds the information for the nodes of the tree that gets generated for the minimax algorithm each node stores a current state of the board,
#the action/move that it took to generate the node, the minimax value which gets defaulted to -999, and its children nodes
class node:
    def __init__(self, state, action):
        self.state = state
        self.action = action
        self.minimaxValue = -999
        self.children = []
    
    #this function iteratively generates all its children(one for each possible move from the current state of the board)
    def generateChildren(self, move):
        #this if statement generates all the possible moves based on whos turn it is to move 
        if move == "black":
            workingEnv = ChessEnvV2(initial_board=self.state["board"], opponent=nullmove, player_color="BLACK")
        else:
            workingEnv = ChessEnvV2(initial_board=self.state["board"], opponent="none")
        #this retrives the possible moves and then loops through and creates a child for each one 
        possibleActions = workingEnv.possible_actions
        for action in possibleActions:
            new_state, reward, done, info = workingEnv.step(action)
            chNode = node(new_state, action)
            self.children.append(chNode)
            #this undoes the move so we can generate the next one
            workingEnv.reset()

#this is nothing realted to the algorithm it is just needed for the library to function as intended 
def nullmove(env):
    board = env.state["board"]
    for rowInd in range(len(board)):
        for colInd in range(len(board[0])):
            if board[rowInd][colInd] == 1 or board[rowInd][colInd] == -1:
                return ((rowInd,colInd), (rowInd,colInd))

#this is a helper function that takes in the children and then returns the highest minimax value out of all of them
def max(children):
    maxVal = -100

    for child in children:
        if child.minimaxValue > maxVal:
            maxVal = child.minimaxValue
        
    return maxVal
    
#this is a helper function that takes in the children and then returns the lowest minimax value out of all of them
def min(children):
    minVal = 100

    for child in children:
        if child.minimaxValue < minVal:
            minVal = child.minimaxValue

    return minVal
