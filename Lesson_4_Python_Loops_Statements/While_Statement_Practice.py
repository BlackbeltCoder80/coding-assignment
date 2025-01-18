# "While Statements", keeps running the code as long as the condition holds true.

marshmallows = 0
while marshmallows < 5:
    marshmallows +=1
    print( "Add a marshmallow! Now there are" " " + str(marshmallows) + " " "marshmallows")

#initialize a varible
temperature = 100
# Setup a while loop with condition that is never true
while temperature < 0:
    #This block of code will not execute becasue the initial temperature is 100, which is not less than 0
 temperature -= 1
print("temperature is now:", temperature)
    # Since the loop body never executes, this print statement will run immediately
print("The temperature was never below 0 to begin with.")
while True:
   user_input = input("Say 'stop' to end the refill: ")
   if user_input.lower() == 'stop':
      break
   else:
      print("Here's more coffee!")