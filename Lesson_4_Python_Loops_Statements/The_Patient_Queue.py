# Use While loop to manage a queue system.
# What will I need in a queue? "List", Time, Remove form index"
# Needed Items:
# time module "input time" 
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

patients = 5
#While 5 > 0
while patients > 0: # Creates a loop that conintues until patients ==0
    print(f"Patients number {patients} please come in.")
    patients -= 1 # patients == 5 -1 => patients = 4

print("There are no more patients in the queue.")
        
    
    
    

