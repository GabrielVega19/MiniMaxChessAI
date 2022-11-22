import gym
from gym_chess import ChessEnvV1, ChessEnvV2
from library import utilityFunction, inputToTouple
from minimaxTree import minimaxTree

#choose difficulty of the chess ai easy(2), medium(3), hard(4) behind the scened the difficulty will be determined by setting the depth limit to different values 
inv = True
while inv:
    inp1 = input("What difficulty would you like to play at(Easy, Medium, Hard): ")
    if inp1 == "easy":
        difficulty = 2
        inv = False
    elif inp1 == "medium":
        difficulty = 3
        inv = False
    elif inp1 == "hard":
        difficulty = 4
        inv = False

#this function is called by the library to preform the move of the opponent behind the scenes it runs the minimax algorithm 
def minimaxMove(env):
    print("**********Your Move************")
    env.render()
    tree = minimaxTree(env.state, difficulty)
    tree.generateTree(tree.headNode, 0)
    tree.runMiniMaxAlgorithm()
    return tree.returnBestMove(env)   

#Creates the environment and passes in the function for the opponent move calculation 
env = ChessEnvV2(opponent=minimaxMove)

# This is the main gameplay loop, It only stops when you or the opponent is calculated to have won 
while True:
    #prints out the initial state of the board on the first loop and then the opponents move on all other loops
    print("**********Thier Move************")
    env.render()

    #Asks the user for input of which piece they want to move expects valid input for board
    piece = input("Input which piece you want to move (ex. e2): ")
    while not len(piece) == 2:
        piece = input("Input which piece you want to move (ex. e2): ")
    #turns the input into a touple
    t1 = inputToTouple(piece)
    #Asks the user for input of where they want to move it to 
    space = input("Input where you want to move (ex. e2): ")
    while not len(space) == 2:
        space = input("Input where you want to move (ex. e2): ")
    #turns the input into a touple
    t2 = inputToTouple(space)
    #turns the input touples into a touple for the library to use
    move = (t1, t2)
    #turns the move into an action which can be applied to the board
    action = env.move_to_action(move)

    # Applys the action that was generated from user input to the board then passes to the opponents move 
    new_state, reward, done, info = env.step(action)
    
    #check to see if you won 
    if done:
        print("Congradulations you won")
        break
