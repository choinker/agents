
#totalUpdates = 1000
#eps = 100
#explorePercentage = 0.1

#for update in range(totalUpdates):
#   finalExplorationUpdate = explorePercentage * totalUpdates
#   if (update < finalExplorationUpdate):
#      explorationRatio = update / finalExplorationUpdate
#      eps = eps * (1 - explorationRatio)
#   else:
#      eps = 0

#   print(str(eps))



# Set epsilon
# Set duration of exploration

# Set endExploration = explorePercentage * totalUpdates

# Anneal epsilon from 100 -> 1 over the start -> endExploration 
# if update < endExploration
#   epsilon = epsilon * (1 - 


eps = 100

totalUpdates = 1000
explorePercentage = 0.5

explorationUpdates = totalUpdates * explorePercentage

# This decrement over exploration will anneal your epsilon to 0
epsDecrement = 100 / explorationUpdates

print(explorationUpdates)
print(epsDecrement)

for update in range(totalUpdates):
   if update < explorationUpdates:
      eps = eps - epsDecrement
   eps = max(0, eps)
   print("update: " + str(update) + "    eps: " + str(eps))
   
