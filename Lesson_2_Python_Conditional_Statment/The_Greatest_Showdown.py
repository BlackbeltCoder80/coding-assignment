# Task 1: Identify the Greatest 
# Write a Python program that asks the user to enter three numbers. 
# Your code should then identify and print out the largest number among the three.

number_1 = int(input ("Enter the first numebr that comes to your mind: "))
number_2 = int(input("Enter the second numer that comes to your mint:"))
number_3 = int(input("Enter the final number that comes to your mind: "))
if number_1 > number_2 and number_1 > number_3:
    print(number_1, "Is The greatest")
elif number_2 > number_1 and number_2 > number_3:
    print(number_2, "Is The Greatest")
elif number_3 > number_1 and number_3 > number_1:
    print(number_3, "Is The Greatest")
else:
    print("They are all equal")

#Task 2: Identify the Smallest Improve upon your code from 
# Task 1 to also determine the smallest number among the three and print it out.
#Expected Outcome: If we provide the numbers 3, 3, and 4, it should print out that 
# "The smallest number is 3. The largest number is 4. "

number_1 = int(input ("Enter the first numebr that comes to your mind: "))
number_2 = int(input("Enter the second numer that comes to your mint:"))
number_3 = int(input("Enter the final number that comes to your mind: "))
if number_1 > number_2 and number_1 > number_3 and number_2 < number_3:
    print(number_1, "Is The greatest and", number_2, "is the smallest")
elif number_2 > number_1 and number_2 > number_3 and number_3 < number_1:
    print(number_2, "Is The Greatest and", number_3, "is the smallest")
elif number_3 > number_1 and number_3 > number_2 and number_1 > number_2:
    print(number_3, "Is The Greatest and", number_1, "is the smallest")
else:
    print("Equal")