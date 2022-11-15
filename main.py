import gym
from gym_chess import ChessEnvV1, ChessEnvV2
from library import utilityFunction, inputToTouple
import random

#choose difficulty of the chess easy(3), medium(6), hard(9) ai will be determined from depth limit  
inp1 = input("What difficulty would you like to play at(Easy, Medium, Hard): ")
if inp1 == "easy":
    difficulty = 3
elif inp1 == "medium":
    difficulty = 6
elif inp1 == "hard":
    difficulty = 9
else:
    inp1 = input("Please enter Easy, Medium, or Hard: ")


#Creates the environment 
env = ChessEnvV2()
env = gym.make('ChessVsSelf-v2')
env.reset()

# Shows state of board
env.render()
# Loop need to change to stop at win condition 
for i in range(100):
    #Asks the user for input and then turns it into a move
    piece = input("Input which piece you want to move (ex. e2): ")
    while not len(piece) == 2:
        piece = input("Input which piece you want to move (ex. e2): ")
    t1 = inputToTouple(piece)
    space = input("Input which piece you want to move (ex. e2): ")
    while not len(space) == 2:
        space = input("Input which piece you want to move (ex. e2): ")
    t2 = inputToTouple(space)
    move = (t1, t2)
    #turns the move into an action 
    action = env.move_to_action(move)
    
    # Apply move and show board
    new_state, reward, done, info = env.step(action)

    # Then display ai is moving and generate ai’s move
        #print out something to show ai is moving
        #use minimax to generate move
            #need to make a utility function                                                                                            
            #Make the tree
                #Nodes of board state(for utility function), move that was used to get there, and the minimax value
                #stop at dificulty value selected in the beggining 
            #start from bottom of the tree and then go upwards
            #you would look at children chose the one with the chosen minimax value then chose the move at that child node
        #turn move into action 
    # Show board after ai’s move
        #apply move to the board from the action
