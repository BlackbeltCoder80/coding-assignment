# For Lools Festival Planner: Utilize to iterate over multiple lists and 
# organize event details withouht using functions

#
attendees = ["40_kids", "80_adults", "20_young_adults"]
play_ground = ["play_grnd_1", "play_grnd_2", "play_grnd_3"]
#Playgorunds can hold only kids and only 10 kids a play ground
#The theater can hold mixture of kids, adults and young adults. However both theaters combined can hold only 100 total.
theater = ["theater_1", "theather_2"]
#The water slide can hold only 20 people each.
water_slam = ["water_slam_1", "water_slam_2"]

for kids in attendees:
    print(attendees [0:1])
kids = 40
adults = 80
young_adults = 20
attendees_kids = attendees [0] # 40_kids
attendees_kids


# Extract number of kids
attendees_kids = attendees[0]  # "40_kids"
kids_count = int(attendees_kids.split("_")[0])  # Extract "40"

# Allocate kids to playgrounds
for playground in play_ground:
    if kids_count > 0:
        if kids_count >= 10:
            print(f"Assigning 10 kids to {playground}")
            kids_count -= 10
        else:
            print(f"Assigning {kids_count} kids to {playground}")
            kids_count = 0  # All kids are assigned

booth_types = ["Food", "Games", "Music", "Craft"]
schedule_times =["10:00", "1:00pm", "3:00p", "5:00pm"]
items_needed = ["grill", "Tickets", "Instruments", "Paint"]

for i in range(len(booth_types)):
    booth = booth_types[i]
    time = schedule_times[i]
    item = items_needed[i]
    print(f"{booth} Booth - Schedule: {time} Itme need: {item}")
    #Updated
    print(kids)

