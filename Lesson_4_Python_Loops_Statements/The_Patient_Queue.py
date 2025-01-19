# Use While loop to manage a queue system.
# What will I need in a queue? "List", Time, Remove form index"
# Needed Items:
# time moudle "input time" 
# Who will be in a Queue "People"
# How long they will be in the Queue? "60 seconds"
import time
people_in_queue = ["David", "Robert", "Lisa", "Mickey"]
queue_timer = 10
while people_in_queue:
    queue_time = queue_timer
    while queue_time > 0:
        print(f"{people_in_queue[0]} you have {queue_timer} seconds remaining")
        time.sleep(1)
        queue_time -= 1
        if queue_time == 0:
            print(f"{people_in_queue[0]}: Your time is Up!")
            people_in_queue.pop(0)
            if people_in_queue:
                print(f"{people_in_queue[0]} you are next!")
            else:
                print("Queue is empty!")
        
    
    
    

