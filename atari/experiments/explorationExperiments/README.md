This folder contains exploration related experiments

Experiment 1: fully random action selection

![Results](https://github.com/andrewgough94/agents/blob/master/atari/experiments/explorationExperiments/openai-2018-04-13-16-59-23-675036/Figure_1.png)

16 Environments

nohup python3.6 -m baselines.a2c.run_atari --env SpaceInvadersNoFrameskip-v0 &

------------------------------------------------------------------------

Experiment 2: random (blue) vs. greedy (green)

![Results1](https://github.com/andrewgough94/agents/blob/master/atari/experiments/explorationExperiments/RandomVsGreedy.png)

Graph2: python3 ~/Documents/school/thesis/baselines/baselines/results_plotter.py --dirs openai-2018-04-13-16-59-23-675036/ ../a2cExperiments/spaceinvaders/openai-2018-04-12-21-12-33-874448/ --task_name SpaceInvaders

-------------------------------------------------------------------------

Experiment 3: epsilon-greedy 10% (blue) vs. epsilon-greedy 20% (green) vs. random(red) vs. greedy (cyan)

![Results2](https://github.com/andrewgough94/agents/blob/master/atari/experiments/explorationExperiments/Figure_3.png)

python3 ~/Documents/school/thesis/baselines/baselines/results_plotter.py --dirs openai-2018-04-16-17-55-49-768980 openai-2018-04-16-18-06-16-410460 openai-2018-04-13-16-59-23-675036/ ../a2cExperiments/spaceinvaders/openai-2018-04-12-21-12-33-874448/ --task_name SpaceInvaders

-------------------------------------------------------------------------

Experiment 4: greedy lr .0007 (blue) vs. greedy learning rate .01 (green)

![Results3](https://github.com/andrewgough94/agents/blob/master/atari/experiments/explorationExperiments/Figure_4.png)

python3 ~/Documents/school/thesis/baselines/baselines/results_plotter.py --dirs openai-2018-04-18-11-45-35-796746/ openai-2018-04-18-11-55-15-218135/ --task_name SpaceInvaders --num_timesteps 11000000


Atari SpaceInvader Experiments using A2C
-------------------------------------------------------------------------

Random Policy - openai-2018-04-13-16-59-23-675036

Epsilon-Greedy (10%) - openai-2018-04-16-17-55-49-768980

Epsilon-Greedy (20%) - openai-2018-04-16-18-06-16-410460

Vanilla A2C - openai-2018-04-18-11-45-35-796746

Learning Rate (.01) - openai-2018-04-18-11-55-15-218135


