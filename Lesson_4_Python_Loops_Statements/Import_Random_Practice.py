import random

#Let's roll the dice 10 times
for _ in range(10): # Express how many time to rolled dice should be executed.
    dice_roll = random.randint(1, 6) # The dice range or type of dice "d6", 1-6. One and six are inclusive.
    print("You rolled a" " " + str(dice_roll) + "!")

# Exercise Playlist
playlist = ['song1', 'song2', 'song3', 'song4', 'song5' ]
random.shuffle(playlist)

for song in playlist:
    print(song)
    