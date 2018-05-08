This folder contains exploration related experiments

------------------------------------------------------------------------
Experiment 1: vanilla a2c (blue)

![Results1](https://github.com/andrewgough94/agents/blob/master/atari/experiments/explorationExperiments/mspacman/Figure_1.png)

nohup python3.6 -m baselines.a2c.run_atari --env MsPacmanNoFrameskip-v0 --exploration vanilla &

python3 ~/Documents/school/thesis/baselines/baselines/results_plotter.py --dirs openai-2018-04-19-17-49-57-129393/ --num_timesteps 11000000 --task_name MsPacMan

------------------------------------------------------------------------

Experiment 1: random (blue) vs. vanilla (green)

![Results1](https://github.com/andrewgough94/agents/blob/master/atari/experiments/explorationExperiments/RandomVsGreedy.png)

[insert nohup here]

Graph2: python3 ~/Documents/school/thesis/baselines/baselines/results_plotter.py --dirs openai-2018-04-13-16-59-23-675036/ ../a2cExperiments/spaceinvaders/openai-2018-04-12-21-12-33-874448/ --task_name SpaceInvaders

-------------------------------------------------------------------------

Atari Pong Experiments using A2C
-------------------------------------------------------------------------

Random Policy - 

Vanilla A2C - openai-2018-04-19-17-49-57-129393/

Epsilon-Greedy (10%) - 

Epsilon-Greedy (20%) - 
