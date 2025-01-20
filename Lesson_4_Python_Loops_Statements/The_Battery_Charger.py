# Exercise 3
# You are programming a smart battery charger.
# That not only charges battery but also performs checks at certain milestones
# The battery starts at 0% and charges in increments. 
# If the battery reaches 50% efficiency, it charges faster. 
# IF not it slows down to prevent overcharging.
 
# Here are the task you need to perform:
# 1. Initialize a variable to represent the fbattery charge level.
# 2. Use a while loop to charge the battery in increments.
# 3. Inisde the loop, use if satements to check the charge level.
# 4. If the charge level is 50% increase the charging increments.
# 5. If the charger level reaches 80% decreas the charging increments to prevent damage.
# 6. Print the battery levle at each increment and message when the battery is fully charged.

#Hint you will need to adjust the increment value within the while loop on the charge level.
battery = 0
increment = 10
while battery < 100:
    battery += increment
    print(f" Battery is now at {battery}%")
    if battery == 50:
        print("Efficiency check: increaseing charge rate")
        increment = 15
    elif battery == 80:
        print("Efficiency check: Reducing charge rate to prevent overcharge.")
        increment = 5
print("The battery is now fully charged")

        