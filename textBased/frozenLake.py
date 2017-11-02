import gym
import numpy as np

# Displays 1. action_space range and input... 2. observation space that is visible to agent
# env = gym.make('MountainCar-v0')
# print(env.action_space)
# print(env.observation_space)


# DEMO: frozen lake random movements
env = gym.make('FrozenLake-v0')
print(env.action_space)
print(env.observation_space)

env.reset()
scores = []
numEpisodes = 1000

for i_episode in range(numEpisodes):
   # env.reset() restarts the env and returns an initial observation
   observation = env.reset()
   score = 0
   for t in range(100):
      env.render()
      action = env.action_space.sample()
      observation, reward, done, info = env.step(action)
      print("a: {}".format(action))
      print("r: {}".format(reward))
      print("o: {}".format(observation))
      print("i: {}".format(info))
      if done:
         print("Episode finished after {} timesteps".format(t+1))
         scores.append(reward)
         break


print("Avg score of all episodes: {}".format(np.mean(scores)))
