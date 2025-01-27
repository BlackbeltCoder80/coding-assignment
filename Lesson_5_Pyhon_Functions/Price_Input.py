while True:
    price = float(input("Enter the prine"))
    rounded_price = round(price, 2)
    print(f"ORunded Price: ${rounded_price}")

    new_price = input('Would you like to enter in a new price? (yes/no)').lower()
    if new_price != 'yes':
        break