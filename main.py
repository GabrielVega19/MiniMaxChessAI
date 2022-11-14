import gym
from gym_chess import ChessEnvV1, ChessEnvV2


#choose difficulty of the chess easy(3), medium(6), hard(9) ai will be determined from depth limit  
# Shows state of board
# Loop
    # Enter prompt for piece and move (requires correct move)
        #turn input into touple of touples ex ((6,0), (5,0))
        #turn into action
    # Apply move and show board
        #apply move to the board from the action
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



env = ChessEnvV2()
env = gym.make('ChessVsSelf-v2')
env.reset()

currentState = env.state
moves = env.possible_moves
action = env.move_to_action(moves[0])

newState, reward, done, info = env.step(action)

print(currentState)

env.render()

