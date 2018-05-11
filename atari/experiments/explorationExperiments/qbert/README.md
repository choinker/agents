Atari Qbert Experiments using A2C
---------------------------------------------
Notes: lr = .001, 


Experiment 1: vanilla (blue)
This graph shows that the reward distribution is interesting, 'step-ladder' of reward, shows that agent is clearly mastering certain sequences of the environment, graph is reward over time plot including variance

![Results1](https://github.com/andrewgough94/agents/blob/master/atari/experiments/explorationExperiments/qbert/Figure_1.png)

Graph1: python3 ~/Documents/school/thesis/baselines/baselines/results_plotter.py --dirs openai-2018-04-18-18-30-48-074460 --num_timesteps 11000000 --task_name Qbert

----------------------------------------------

Experiment 2: random (blue)
This graph is a completely random policy attempting to play Qbert, including variance

![Results2](https://github.com/andrewgough94/agents/blob/master/atari/experiments/explorationExperiments/qbert/Figure_2.png)

Graph2: python3 ~/Documents/school/thesis/baselines/baselines/results_plotter.py --dirs openai-2018-04-19-14-26-35-458738 --num_timesteps 11000000 --task_name Qbert

----------------------------------------------

Experiment 3: vanilla (blue) vs. random (green)

![Results3](https://github.com/andrewgough94/agents/blob/master/atari/experiments/explorationExperiments/qbert/Figure_3.png)

Graph3: python3 ~/Documents/school/thesis/baselines/baselines/results_plotter.py --dirs openai-2018-04-18-18-30-48-074460 openai-2018-04-19-14-26-35-458738 --num_timesteps 11000000 --task_name Qbert

-----------------------------------------------

Experiment 4: random (blue) vs. vanilla a2c (green) vs. annealing at 5% a2c (red)

Analysis: Qbert is a dense reward game and both vanilla and annealing agents take a while to catch onto any substantial reward. Around 4M timesteps annealing agent performance surpasses vanilla until 5M timesteps where vanilla catches back up. The two are neck and neck for the rest of training process aside from some serious policy failures by vanilla. In the tail end of training vanilla achieves a significant performance boost. 

![Results4](https://github.com/andrewgough94/agents/blob/master/atari/experiments/explorationExperiments/qbert/QbertRandVanAnneal.png)

Graph4: python3 ~/Documents/school/thesis/baselines/baselines/results_plotter.py --dirs openai-2018-04-19-14-26-35-458738 openai-2018-04-18-18-33-40-747137 openai-2018-05-09-16-24-27-691293 --num_timesteps 11000000 --task_name Qbert

-----------------------------------------------

Vanilla A2C QbertNoFrameskip-v0 - openai-2018-04-18-18-30-48-074460

Vanilla A2C QbertNoFrameskip-v4 - openai-2018-04-18-18-33-40-747137

Random Policy QbertNoFrameskip-v0 - openai-2018-04-19-14-26-35-458738

Annealing at 5% - openai-2018-05-10-11-20-33-761893

A2C e-greedy constant 10% QbertNoFrameskip-v0 - openai-2018-04-19-17-36-34-655298 : Failure, can't learn

A2C e-greedy constant 20% QbertNoFrameskip-v0 - openai-2018-04-19-17-44-21-992084 : Failure, can't learn
