Space Invaders experiments with A2C

Default unless specified otherwise



Experiments Below: openai-2018-04-12-21-12-33-874448  openai-2018-04-14-14-36-45-750295 
Expected Results: both experiments exact same, should yield exact same results
Actual: Differ in their path, similar in final score


![Results](https://github.com/andrewgough94/agents/blob/master/atari/experiments/a2cExperiments/spaceinvaders/Figure_1.png)

python3 ~/Documents/school/thesis/baselines/baselines/results_plotter.py --dirs openai-2018-04-12-21-12-33-874448/ openai-2018-04-14-14-36-45-750295/ --task_name SpaceInvadersNoFrameskip-v0


-----------------------------------------------------------------------------------------------------------------
Experiments Below: openai-2018-04-15-15-38-57-426628/ openai-2018-04-15-15-41-04-785781/
Expected: Should yield exact same results
Actual: Differ in their path, similar in final score

![Results](https://github.com/andrewgough94/agents/blob/master/atari/experiments/a2cExperiments/spaceinvaders/Figure_2.png)

python3 ~/Documents/school/thesis/baselines/baselines/results_plotter.py --dirs openai-2018-04-15-15-38-57-426628/ openai-2018-04-15-15-41-04-785781/ --task_name SpaceInvadersNoFrameskip-v4
