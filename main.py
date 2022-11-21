import gym
from gym_chess import ChessEnvV1, ChessEnvV2
from library import utilityFunction, inputToTouple
from minimaxTree import minimaxTree

#choose difficulty of the chess easy(3), medium(6), hard(9) ai will be determined from depth limit  
inp1 = input("What difficulty would you like to play at(Easy, Medium, Hard): ")
if inp1 == "easy":
    difficulty = 1
elif inp1 == "medium":
    difficulty = 2
elif inp1 == "hard":
    difficulty = 3


def minimaxMove(env):
    print("**********Your Move************")
    env.render()
    tree = minimaxTree(env.state, difficulty)
    tree.generateTree(tree.headNode, 0)
    tree.runMiniMaxAlgorithm()
    return tree.returnBestMove(env)
    

    # Then display ai is moving and generate ai’s move

        #print out something to show ai is moving
        #use minimax to generate move                                                                                    
            #Make the tree
                #Nodes of board state(for utility function), move that was used to get there, and the minimax value
                #stop at dificulty value selected in the beggining 
            #start from bottom of the tree and then go upwards
            #you would look at children chose the one with the chosen minimax value then chose the move at that child node
        #turn move into action 
    # Show board after ai’s move
        #apply move to the board from the action
        #check to see if they won
    


#Creates the environment 
env = ChessEnvV2(opponent=minimaxMove)


# Loop untill win condition
while True:
    print("**********Thier Move************")
    env.render()
    #Asks the user for input and then turns it into a move
    piece = input("Input which piece you want to move (ex. e2): ")
    while not len(piece) == 2:
        piece = input("Input which piece you want to move (ex. e2): ")
    t1 = inputToTouple(piece)
    space = input("Input where you want to move (ex. e2): ")
    while not len(space) == 2:
        space = input("Input where you want to move (ex. e2): ")
    t2 = inputToTouple(space)
    move = (t1, t2)
    #turns the move into an action 
    action = env.move_to_action(move)
    # Apply move and checks to see if you won
    new_state, reward, done, info = env.step(action)
    #check to see if you won 
    if done:
        print("Congradulations you won")
        break
