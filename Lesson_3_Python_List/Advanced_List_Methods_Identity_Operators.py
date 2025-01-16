#2. Advanced List Methods and Identity Operators

#Problem Statement: You have two lists of student names. 
# One list contains the names of students who have submitted their assignments, 
# and the other list contains the names of students who attended the last class.

#Task 1: Given the two lists:

submitted = [ "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Frank"]

print("Alice" in submitted, "Alice" in attended)
#Find out if Alice submitted their assignment and attended class. HINT: How might the in keyword be of use here? 
# And how can you check to see if Alice is in both submitted and attended in one if statement?

# This should have been easy to figure out but I decided to just ask myself questions to figure this out...

# Is Alice in the submitted list? Yes
# IS Alice in the attended list? Yes
# Find out if Alcie is in list.
# I tried it a few ways print with in keyword
if "Alice" in submitted and "Alice" in attended:
    print("Alice was in class and turned in her assignment.")
if "Alice" in attended and "Alice" not in submitted:
    print("Alice was in class but did not submit her assignment")

if "Alice" in submitted and "Alice" in attended:
    print("Alice was in class and turned in her assignment.")
elif "Alice" in attended and "Alice" not in submitted:
        print("Alice was in class but did not submit her assignment")
elif "Alice" in submitted and "Alice" not in attended:
     print("Alice wasnt in class but turned in her assignment")
else:
     print("Alice was not in class and did not submit her assignment")

