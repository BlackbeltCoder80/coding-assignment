# Import Random module
# Use Random Shuffle
# USe for loop to iterate through the shuffle list and present each question.quit
# Print out each question.


import random

question = [' What is the color', ' What is the height', 'What color are both']

random.shuffle(question)


for question in question:
     print(question)