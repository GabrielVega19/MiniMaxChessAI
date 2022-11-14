import gym
from gym_chess import ChessEnvV1, ChessEnvV2

env = ChessEnvV2()
env = gym.make('ChessVsSelf-v2')
env.reset()

currentState = env.state
moves = env.possible_moves
action = env.move_to_action(moves[0])

currentState, reward, done, info = env.step(action)


env.render()

