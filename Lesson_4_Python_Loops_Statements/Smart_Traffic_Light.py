traffic_light_colors = ["Red", "Yellow","Green", "Yellow"]
green_count = 0

while True:
    for color in traffic_light_colors:
        print(f"The Traffic light is now{color}.")
        if color == 'Green':
            green_count += 1
            if green_count == 3:
                print("Maintenance time! The cycle will stop.")
                break

    if green_count == 3:
        break