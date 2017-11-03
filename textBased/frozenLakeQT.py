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
print([env.observation_space.n,env.action_space.n])

# Initialize table with all zeros
Q = np.zeros([env.observation_space.n,env.action_space.n])

# Set learning parameters
lr = .8
y = .95

env.reset()
scores = []
numEpisodes = 394

for i_episode in range(numEpisodes):
   # env.reset() restarts the env and returns an initial observation
   state = env.reset()
   score = 0
   for t in range(100):
      env.render()
      action = env.action_space.sample()
      action = np.argmax(Q[state,:] + np.random.randn(1,env.action_space.n)*(1./(i_episode+1)))

      state1, reward, done, info = env.step(action)
      Q[state, action] = Q[state, action] + lr*(reward + y*np.max(Q[state1,:]) - Q[state, action])
      #print("a: {}".format(action))
      #print("r: {}".format(reward))
      #print("o: {}".format(state1))
      #print("i: {}".format(info))
      #print(Q)
      #print("\n")

      state = state1
      if done:
         print("Episode finished after {} timesteps".format(t+1))
         scores.append(reward)
         break


print("Avg score of all episodes: {}".format(np.mean(scores)))
