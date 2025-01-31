# Objective: To practice the use of shorthand if statements.

# Task 1: Code Correction You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.

# Buggy Code:

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
if attendees >= 100 and venue == "large hall":
    print("you will need a projector and audio system")
elif attendees <= 100 and venue == "conference room":
    print("An audio system will be just enough for your event")
catering_choice = input("Would you like vegetarian food? (yes/no): ")
if catering_choice == "yes":
    print("I recommend, Veggie Delight Cateres.")
else:
    print("I recommed, Gourmet Meals Caterers.")
# Task 2: Venue Selection

# Based on the corrected code from Task 1, further enhance your code to recommend additional things like "audio system" or "projector" based on the number of attendees.

# Task 3: Catering Choices

# Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".

# NOTE: Ensure that all code in your file is ready to run. This means that if someone opens your file and clicks the run button at the top, all code executes as intended. For example, if there are if statements or print statements, they should function correctly and display output in the console as expected.

# The goal of this note is to ensure that all code in your Python file runs smoothly and that is has been tested.