count = 10
landed_numbers = []

while count > 0:
    count -= 1
    if count % 2 == 1:
        continue
    landed_numbers.append(count)
print("Numbers landed on:", landed_numbers[::-1])
