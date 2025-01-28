room_temperature = [ 22, 24, 19, 21]
room_names = ["livingroom", "kitchen", "bedroom", "bathroom"]

warmest_temp = max(room_temperature)
coolest_temp = min(room_temperature)

warmest_room_index = room_temperature.index(warmest_temp)
coolest_room_index = room_temperature.index(coolest_temp)

warmest_room = room_names[warmest_room_index]
coolest_room = room_names[coolest_room_index]

print(f" The {warmest_room} is the warmest with {warmest_temp}")
print(f" The {coolest_room} is the warmest with {coolest_temp}")

