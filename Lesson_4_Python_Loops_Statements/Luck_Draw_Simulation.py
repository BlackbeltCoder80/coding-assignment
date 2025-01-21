# Import the random module to use its choice selection capabilities.
# Create a list of particular names, inlcuding 'Alex'
# Use a while loop to repeatedly draw a name randomly form the list of participants.
#The lfoop sshould only terminate when 'Alex' is drawn.
# Ensure that the loop doe snot produce any output until 'Alex' is drawn.

import random
participants = [ 'John', 'Lila', 'Sarah', 'Alex', 'Max']
while 'Alex' not in random.choice(participants, k=1):
    pass

print("Congratulations, Ales! You've wom the lucky draw")