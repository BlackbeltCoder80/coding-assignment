# 2. Double Scoop with Nested Loops
#Objective: The aim of this assignment is to practice using nested loops in Python.

#Task 1: Your Mood Tracker Simulate a mood tracker 
# that records your mood at three different times of the day (morning, afternoon, evening) for each day of the week. 
# Use nested loops to implement this: the outer loop should iterate over the days, and 
# the inner loop should iterate over the times of the day. 
# For each time, randomly select a mood from a predefined list and print it. 
# Use the random module again to randomly select the mood.

#Example Outcome: An example would be "On Tuesday afternoon you were sad" "On Tuesday night you were happy" "On Wednesday morning you were tired"

#NOTE: Ensure that all code in your file is ready to run. This means that if someone opens your file and clicks the run button at the top, all code executes as intended. For example, if there are if statements, print statements, or for loops, they should function correctly and display output in the console as expected.

#The goal of this note is to ensure that all code in your Python file runs smoothly and that is has been tested.
import random

mood_list = ["Sad", "Happy", "Angry", "Excited"]
time_of_day = ["morning", "afternoon", "evening" ]
days_of_week = ["Mondy", "Tuesday", "Wednesday", "Thurday", "Friday", "Saturday", "Sunday"]

for i in range(len(days_of_week)):
    mood = random.choice(mood_list)
    day = random.choice(time_of_day)
    print(f"On {days_of_week[i]}, {day} you were feeling {mood}")

    # Awesome just built off the first code made it much easier... Also I got this memorized now at least I hope so lol...
    # I really appreciate you guys and your work. Ive really enjoyed being here workign with you guys.
    # I really hope to return with more knowldege to expand and or send my own team here one day. 
    # Huge Thanks.