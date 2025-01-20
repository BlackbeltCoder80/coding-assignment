coffee_resevoir = 10
coffee_types = ["Espressp", "Cappuccion", "Latte", "Americano Mocha"]

while coffee_resevoir > 0:
    if coffee_types:
        current_coffee = coffee_types.pop(0)
        print(f"Dispensing {current_coffee}")

        coffee_resevoir -= 1
        print(f"Coffe types left: {coffee_types} ")
    else:
        print("No more coffee types available.")
        break
        print("The coffe resevoir is empty")