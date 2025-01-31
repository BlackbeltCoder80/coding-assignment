# 1. Python List Transformation
#Objective: The aim of this assignment is to practice list operations and transformations.

#Problem Statement: You've been given a list of grades from an exam. You need to process and analyze these grades.

#Task 1: Given the list of grades:

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
sorted_grades_descending = sorted(grades, reverse=True)
print(sorted_grades_descending) # Bam! 

# Going to use sorted to sort list however need to use reverse to change the list. Had to figure out how to use reverse in the middle of a string but it seems to work just fine.
#Sort the grades in descending order and print the sorted list.

#Task 2: Calculate the average grade and print it.
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
sorted_grades_descending = sorted(grades, reverse=True)
print(sorted_grades_descending) # Bam! 

grades_added = sum(grades)
print(grades_added)
Total_Grade_Count = len(grades)
average = grades_added / Total_Grade_Count
print(average)

# Calculating average grade will be tricky...r
#2. Advanced List Methods and Identity Operators
#Problem Statement: You have two lists of student names. One list contains the names of students who have submitted their assignments, and the other list contains the names of students who attended the last class.

#Task 1: Given the two lists:

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
#Find out if Alice submitted their assignment and attended class. HINT: How might the in keyword be of use here? And how can you check to see if Alice is in both submitted and attended in one if statement?