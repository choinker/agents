This folder contains exploration related experiments

------------------------------------------------------------------------

Experiment 1: vanilla (blue) vs. random (green)

![Results1](https://github.com/andrewgough94/agents/blob/master/atari/experiments/explorationExperiments/pong/Figure_1.png)

Note: Learning rate of .001 instead of .0007

nohup python3.6 -m baselines.a2c.run_atari --env PongNoFrameskip-v0 --exploration vanilla &

Graph: python3 ~/Documents/school/thesis/baselines/baselines/results_plotter.py --dirs openai-2018-05-08-12-37-28-836674/ openai-2018-04-19-18-08-58-010282/ --num_timesteps 11000000 --task_name Pong

------------------------------------------------------------------------

Experiment 2: vanilla lr = .001 (blue) vs vanilla lr = .0007 (green)

![Results2](https://github.com/andrewgough94/agents/blob/master/atari/experiments/explorationExperiments/pong/Figure_2.png)

Graph2: python3 ~/Documents/school/thesis/baselines/baselines/results_plotter.py --dirs openai-2018-05-08-12-37-28-836674/ openai-2018-05-08-12-31-16-905927/ --num_timesteps 11000000 --task_name Pong

------------------------------------------------------------------------

Experiment 3: random (blue) vs. vanilla a2c (green) vs. annealing at 5% a2c (red)

Analysis: Both vanilla and annealing a2c agents are able to solve the Pong environment, however annealing a2c agent solves it roughly 2M timesteps faster than vanilla leading to a much more efficient learning curve.

![Results3](https://github.com/andrewgough94/agents/blob/master/atari/experiments/explorationExperiments/pong/PongRandVanAnneal.png)

Graph3: python3 ~/Documents/school/thesis/baselines/baselines/results_plotter.py --dirs openai-2018-04-19-18-08-58-010282/ openai-2018-05-08-12-37-28-836674 openai-2018-05-09-16-27-41-396915 --num_timesteps 11000000 --task_name Pong


-------------------------------------------------------------------------

Atari Pong Experiments using A2C
-------------------------------------------------------------------------

Random Policy - openai-2018-04-19-18-08-58-010282

Vanilla A2C lr = .0007 - openai-2018-05-08-12-31-16-905927

Vanilla A2C lr = .001 - openai-2018-05-08-12-37-28-836674

Vanilla A2C lr = .01 (Failure couldn't learn) - openai-2018-05-08-12-40-32-613761

Annealing at 5% - openai-2018-05-11-12-00-16-046233

Epsilon-Greedy (10%) - 

Epsilon-Greedy (20%) - 
