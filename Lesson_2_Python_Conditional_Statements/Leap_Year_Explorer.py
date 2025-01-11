#Task 1: Leap Year Checker Write a Python program that prompts the user to input a year. 
# The program should determine if the given year is a leap year or not and then display an appropriate message. 
# Please note that this is the definition of a leap year: 
# Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400.

#Get input from user
year = int(input("Enter Your Birth Year. Lets see if your birthday is in a leap year: ")) 
#Check is the yea ris a leap year
if year % 400 == 0:
    print(f"Your birthday {year} is a leap year")
elif year % 100 == 0:
    print(f"Your Birth {year} is not a leap year")
else:
    print("Try a different birthday")