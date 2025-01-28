print("You woke up in a mysterious forest. Two paths lie before you.")

choices = ["left", "right"]
outcomes = ["You encounter a friendly elf who offers you a map.",
            "You stumble upon a sleeping dragon"]

print(f"Do you go left or right? (Type 'left' or 'right')")
decision = input().lower()

if decision not in choices:
    print("Confused you decide to wait")
elif decision == "left":
    outcomes_index = choices.index("left")    
    print(outcomes_index)
    print(outcomes[outcomes_index])
else:
    outcomes_index = choices.index("right")
    print(outcomes[outcomes_index])
