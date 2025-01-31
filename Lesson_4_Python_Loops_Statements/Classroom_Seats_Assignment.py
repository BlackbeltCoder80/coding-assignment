# Use for loops with the range function to assign seats in classroom settings.
class_students = ["Alice", "Joe", "Beccy"]
seats_room =["Desk 1", "Desk 2", "Desk 3"]

for i in range(len(class_students)):
    for i in range(len(seats_room)):
        print(f" {class_students} will be assigned to {seats_room} today")

        #30 Students - 5 rows
        #Each row can seat an equal number of students.
        #USe a for loop with the range function to assign and print a seat number for each student
        #Seat numbers should start at 1 and increase sequentially.

        total_students = 30
        rows = 5
        students_per_row = total_students // rows 
        for row in range(1, rows +1):
            for seat in range(1, students_per_row + 1):
                seat_number =(row-1) * students_per_row + seat
                print(f"Row{row} - Seat {seat}: Students {seat_number}")