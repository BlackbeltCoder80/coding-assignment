#Use "While" to create a countdown timer while 
# What do I need?
# I need a number to start with. Which means I may need a number.

#I need a end point
# How will timer be set? Input or set time? Do we need to inport anything?
import time
count_down_timer = int(input("Please enter countdown time in seconds"))
while count_down_timer >= 0:
    print(f"Time remaining: {count_down_timer} seconds")
    time.sleep(1)
    count_down_timer -= 1

    if count_down_timer == 30:
        print(f"You have {count_down_timer} Second left. ")
    elif count_down_timer == 10:
        print("time is almost up") # Warning time is up
    elif count_down_timer == 0:
        print("time is up")
        
   