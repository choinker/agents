This folder contains exploration related experiments

------------------------------------------------------------------------
Experiment 1: vanilla a2c (blue)

![Results1](https://github.com/andrewgough94/agents/blob/master/atari/experiments/explorationExperiments/mspacman/Figure_1.png)

nohup python3.6 -m baselines.a2c.run_atari --env MsPacmanNoFrameskip-v0 --exploration vanilla &

Graph1: python3 ~/Documents/school/thesis/baselines/baselines/results_plotter.py --dirs openai-2018-04-19-17-49-57-129393/ --num_timesteps 11000000 --task_name MsPacMan

------------------------------------------------------------------------

Experiment 2: random (blue) vs. vanilla a2c (green)

![Results2](https://github.com/andrewgough94/agents/blob/master/atari/experiments/explorationExperiments/mspacman/Figure_2.png)

Graph2: python3 ~/Documents/school/thesis/baselines/baselines/results_plotter.py --dirs openai-2018-05-09-11-32-38-276102 openai-2018-04-19-17-49-57-129393/  --num_timesteps 11000000 --task_name MsPacMan

-------------------------------------------------------------------------

Experiment 3: random (blue) vs. vanilla a2c (green) vs. annealing at 5% a2c (red)

Analysis: The annealing a2c comes out the gates poorly and has a policy failure about the time that epsilon anneals to zero, but after 6M timesteps it starts to pull away from vanilla a2c performance wise and achieves a peak performance score of 2429.25 over vanilla a2c's 2121.09. Overall vanilla a2c's learning curve appears to be less stable than the annealing epsilon agent.

![Results3](https://github.com/andrewgough94/agents/blob/master/atari/experiments/explorationExperiments/mspacman/MsPacmanRandVanAnneal.png)

Graph3: python3 ~/Documents/school/thesis/baselines/baselines/results_plotter.py --dirs openai-2018-05-09-11-32-38-276102 openai-2018-04-19-17-49-57-129393/ openai-2018-05-09-16-18-38-812531 --num_timesteps 11000000 --task_name MsPacMan

Atari Pong Experiments using A2C
-------------------------------------------------------------------------

Random Policy - openai-2018-05-09-11-32-38-276102

Vanilla A2C - openai-2018-04-19-17-49-57-129393/

Annealing at 5% - openai-2018-05-09-16-18-38-812531

Epsilon-Greedy (10%) - 

Epsilon-Greedy (20%) - 
