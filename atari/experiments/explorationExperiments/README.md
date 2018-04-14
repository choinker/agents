This folder contains exploration related experiments

A2C - fully random action selection

![Results](https://github.com/andrewgough94/agents/blob/master/atari/experiments/explorationExperiments/openai-2018-04-13-16-59-23-675036/Figure_1.png)

16 Environments

nohup python3.6 -m baselines.a2c.run_atari --env SpaceInvadersNoFrameskip-v0 &

--------------------------------------------------------------------

For Reference - greedy (green) vs. random (blue)

![Results1](https://github.com/andrewgough94/agents/blob/master/atari/experiments/explorationExperiments/RandomVsGreedy.png)

Graph2: python3 ~/Documents/school/thesis/baselines/baselines/results_plotter.py --dirs openai-2018-04-13-16-59-23-675036/ ../a2cExperiments/spaceinvaders/openai-2018-04-12-21-12-33-874448/ --task_name SpaceInvaders
