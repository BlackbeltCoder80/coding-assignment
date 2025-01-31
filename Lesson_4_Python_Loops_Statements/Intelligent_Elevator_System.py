current_floor = 5
request_stops =[1, 3, 4]

while current_floor > 0: # While the current floor is greater than 5 run this loop...
    if current_floor in request_stops: # Saying 
        print(f"Stopping at floor {current_floor}")
        request_stops.remove(current_floor)

    current_floor -=1
    print(f"descending to floor {current_floor}")