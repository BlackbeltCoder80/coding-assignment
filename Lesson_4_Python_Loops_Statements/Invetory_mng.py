# Create a list of items in the inventory with theit current quatities.
#Use a for loop to iterate over each item.
#Use an if statement to check if the quantity of an item is below reorder threshold.
#Print out the names of the items that need to be reordered.

inventory =[
    ["Apples", 5],
    ["bananas", 2],
    ["Orange", 0],
    ["Milk", 1],
    ["Eggs", 12]
]

reorder_threshold = 3
for item in inventory:
    name, quantity = item
    if quantity < reorder_threshold:
        print(f"{name} needs to be reordered.")