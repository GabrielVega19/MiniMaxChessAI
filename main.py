import gym
from gym_chess import ChessEnvV1, ChessEnvV2
from library import utilityFunction, inputToTouple
from minimaxTree import minimaxTree
import random

#choose difficulty of the chess ai easy(2), medium(3), hard(4) behind the scened the difficulty will be determined by setting the depth limit to different values 
inv = True
while inv:
    inp1 = input("What difficulty would you like to run simulation at(easy, hard): ")
    if inp1 == "easy":
        difficulty = 2
        inv = False
    elif inp1 == "hard":
        difficulty = 3
        inv = False

#vars to keep track of how many times each player won
aiWins = 0
randomWins = 0
ties = 0
movesToWin = []


#loops the simulation 30 times
for i in range(100):
    #Creates the environment and resets it inbetween turns
    moves = 0
    env = ChessEnvV2(opponent="none")

    # This is the main  loop, it will break when someone wins and the corrosponding counter will be incremented
    while True:
        #checks to see if ai wins
        if env.possible_actions == []:
            aiWins += 1
            movesToWin.append(moves)
            break   

        #choses a random move from all possible moves 
        action = random.choice(env.possible_actions)
        # Applys the action to the board then passes to the opponents move 
        new_state, reward, done, info = env.step(action)
        if done:
            ties += 1
            break

        #begin ai move
        #checks to see if random wins
        if env.possible_actions == []:
            randomWins += 1
            break   

        #initialize tree
        tree = minimaxTree(env.state, difficulty)
        #generate tree
        tree.generateTree(tree.headNode, 0)
        #run algorithm 
        tree.runMiniMaxAlgorithm()
        #turn best move into an action
        action = env.move_to_action(tree.returnBestMove(env))
        #applies the AI move
        new_state, reward, done, info = env.step(action)
        moves += 1
        if done:
            ties += 1
            break


print("After running the simukation 100 times")
print("Times the AI won:", aiWins)
print("Times the Random moves won:", randomWins)
print("Times there was a tie:", ties)
print("Moves it took the AI to win:", movesToWin)
