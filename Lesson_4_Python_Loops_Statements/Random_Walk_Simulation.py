# Import the random module to utilize its random selection
# Define a list of direction that the entitiy can take
# USe a fo rloop to suimulate 10 steps
# In each iteration, randomly select a direction and simulate taking a step in that direction.
# Print out the direction of each step.

import random

directions = ['North', 'South', 'East', 'West']

for step in range(10):
    step_direction = random.choices(directions)
    print(f"Turn {step + 1}: The entity moves 10 steps to the {step_direction}")