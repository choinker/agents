This directory includes an implementation of the A3C algorithm. Based upon Arthur Juliani's Medium Post. In it we use A3C to solve a simple 3D Doom challenge using the VizDoom engine. For more information on A3C, see the accompanying Medium post.

This tutorial requires that VizDoom is installed. It can be easily obtained with:

pip install vizdoom

We also require basic.wad and helper.py, both of which are available from the DeepRL-Agents github repo.

While training is taking place, statistics on agent performance are available from Tensorboard. To launch it use:

tensorboard --logdir=worker_0:'./train_0',worker_1:'./train_1',worker_2:'./train_2',worker_3:'./train_3'
