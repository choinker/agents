This folder contains exploration related experiments

------------------------------------------------------------------------
Experiment 1: vanilla a2c (blue)

![Results1](https://github.com/andrewgough94/agents/blob/master/atari/experiments/explorationExperiments/mspacman/Figure_1.png)

nohup python3.6 -m baselines.a2c.run_atari --env MsPacmanNoFrameskip-v0 --exploration vanilla &

Graph1: python3 ~/Documents/school/thesis/baselines/baselines/results_plotter.py --dirs openai-2018-04-19-17-49-57-129393/ --num_timesteps 11000000 --task_name MsPacMan

------------------------------------------------------------------------

Experiment 1: random (blue) vs. vanilla (green)

![Results1](https://github.com/andrewgough94/agents/blob/master/atari/experiments/explorationExperiments/mspacman/Figure_2.png)

Graph2: python3 ~/Documents/school/thesis/baselines/baselines/results_plotter.py --dirs openai-2018-05-09-11-32-38-276102 openai-2018-04-19-17-49-57-129393/  --num_timesteps 11000000 --task_name MsPacMan

-------------------------------------------------------------------------

Atari Pong Experiments using A2C
-------------------------------------------------------------------------

Random Policy - 

Vanilla A2C - openai-2018-04-19-17-49-57-129393/

Random - openai-2018-05-09-11-32-38-276102

Epsilon-Greedy (10%) - 

Epsilon-Greedy (20%) - 
