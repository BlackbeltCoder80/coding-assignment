# Task 1: Code correction Below is a pieve of Python code with incorrect indentation. Your task is to correct it.
weather = "sunny"

if weather == "sunny":
    print("Wear sunglasses!")
else:
    print("Take an umbrella!")
 
 # Task 2: Your Mood Today Ask the user how they feel today. 
 
 # If they say "happy", 
 # print "That's great to hear!", 
 # and if they say "sad", 
 # print "I hope your day gets better!". 
 # Ensure your if statement is properly indented. HINT: Use the input() function to ask the user how they feel! If you need a refresher, check this out here: https://www.w3schools.com/python/python_user_input.asp\

username = input ("Enter Username:")
print("Hello," + username +"!")
print(username  +  "How do you feel today")
response = input (" (Happy/Sad:) ")
if response.lower() == "happy":
    print("That's great to hear!")
else:
    print("I hope your day gets better!")


