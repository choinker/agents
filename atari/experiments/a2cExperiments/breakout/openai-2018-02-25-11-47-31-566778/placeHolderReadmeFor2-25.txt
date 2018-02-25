MPAC machine 127x37

command: agough@127x37:~/thesis/a3c/baselines $ python3.6 -m baselines.a2c.run_atari

all defaults

usage: run_atari.py [-h] [--env ENV] [--seed SEED]
                    [--num-timesteps NUM_TIMESTEPS]
                    [--policy {cnn,lstm,lnlstm}]
                    [--lrschedule {constant,linear}]

optional arguments:
  -h, --help            show this help message and exit
  --env ENV             environment ID (default: BreakoutNoFrameskip-v4)
  --seed SEED           RNG seed (default: 0)
  --num-timesteps NUM_TIMESTEPS
  --policy {cnn,lstm,lnlstm}
                        Policy architecture (default: cnn)
  --lrschedule {constant,linear}
                        Learning rate schedule (default: constant)
agough@127x37:~/thesis/a3c/baselines $ python3.6 -m baselines.a2c.run_atari

Logging to /tmp/openai-2018-02-25-11-47-31-566778
rockin 16

