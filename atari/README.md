ABOUT

This is a repo containing a DQN implementation with the ability to swap out exploration strategy in action-selection

Modify source code to designate any exploration algorithm

Name output file with command line flag '--out'

EXAMPLE USAGE

```
python3 explorer.py --out experiment1 --explore e-greedy
```

NOTES

Arthur Juliana suggests using a smaller learning rate and larger number of annealing steps to yield better improvements

CartPole is somewhat difficult to solve with DQN, and there is a narrow space within which good hyperparameters exist
