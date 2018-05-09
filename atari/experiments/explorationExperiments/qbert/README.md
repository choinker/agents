Atari Qbert Experiments using A2C
---------------------------------------------
Notes: lr = .01, 


Experiment 1: vanilla (blue)
This graph shows that the reward distribution is interesting, 'step-ladder' of reward, shows that agent is clearly mastering certain sequences of the environment, graph is reward over time plot including variance

![Results1](https://github.com/andrewgough94/agents/blob/master/atari/experiments/explorationExperiments/qbert/Figure_1.png)

Graph 1: python3 ~/Documents/school/thesis/baselines/baselines/results_plotter.py --dirs openai-2018-04-18-18-30-48-074460 --num_timesteps 11000000 --task_name Qbert

----------------------------------------------

Experiment 2: random (blue)
This graph is a completely random policy attempting to play Qbert, including variance

![Results2](https://github.com/andrewgough94/agents/blob/master/atari/experiments/explorationExperiments/qbert/Figure_2.png)

Graph 2: python3 ~/Documents/school/thesis/baselines/baselines/results_plotter.py --dirs openai-2018-04-19-14-26-35-458738 --num_timesteps 11000000 --task_name Qbert

----------------------------------------------

Experiment 3: vanilla (blue) vs. random (green)

![Results3](https://github.com/andrewgough94/agents/blob/master/atari/experiments/explorationExperiments/qbert/Figure_3.png)

Graph 3: python3 ~/Documents/school/thesis/baselines/baselines/results_plotter.py --dirs openai-2018-04-18-18-30-48-074460 openai-2018-04-19-14-26-35-458738 --num_timesteps 11000000 --task_name Qbert


-----------------------------------------------



Vanilla A2C QbertNoFrameskip-v0 - openai-2018-04-18-18-30-48-074460

Vanilla A2C QbertNoFrameskip-v4 - openai-2018-04-18-18-33-40-747137

Random Policy QbertNoFrameskip-v0 - openai-2018-04-19-14-26-35-458738

A2C e-greedy constant 10% QbertNoFrameskip-v0 - openai-2018-04-19-17-36-34-655298 : Failure, can't learn

A2C e-greedy constant 20% QbertNoFrameskip-v0 - openai-2018-04-19-17-44-21-992084 : Failure, can't learn
