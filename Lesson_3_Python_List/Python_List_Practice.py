# Creation a list for fruits
fruits = ["apple", "banana", "cherry"]
#Access List
print(fruits) # Output [apple, banana, cherry]
print(fruits[0]) #output of list "apple"
print(fruits[-1]) # Output of list "cherry"
#List Creation
colors_numebrs = ["blue", 1, "green", 2, "red"]
#Access List
print(colors_numebrs[0])
print(colors_numebrs[4])
print(colors_numebrs[0],colors_numebrs[3])

#List Creation
potions = ["Healing", "Invisibility", "Strength"]
#Acess List last items
print(potions[-1])
#Append List
potions.append("Dexterity")
potions.append("Constitution")
potions.append("Intellegince")
potions.append("Wisdom")
potions.append("Charisma")
potions.append("Bonus Attack")
print(potions[2],potions[3])
#Remove form list
potions.remove("Invisibility")
#del from list
del potions[0] # Output will del Healing from list
print(potions) # Output list 
#.pop() Remove last item from list or specify item to be removed
potions.pop()
print(potions)
#Insert Item with .insert
potions.insert(0, "Ability Modifiers=")
print(potions) #Output current lsit with new insert Ability Modifiers
# Change an itme in the list
potions[0] = "Ability Scores: " # Replace Ability Modifiers =
print(potions)
