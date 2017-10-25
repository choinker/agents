import gym

env = gym.make('MountainCar-v0')
env.reset()
for i_episode in range(20):
   # env.reset() restarts the env and returns an initial observation
   observation = env.reset()
   for t in range(100):
      env.render()
      print(observation)
      action = env.action_space.sample()
      observation, reward, done, info = env.step(action)
      if done:
         print("Episode finished after {} timesteps".format(t+1))
         break
