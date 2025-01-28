while True:
    user_name = input("Please enter you name here:")
    if len(user_name) <=15:
        print("Username is valid")
    else:
        print("Username must be between 5 and 15 characters!")

    continue_input = input ("Do you wnat to try another username? (yes/no)").lower()
    if continue_input != "yes":
        break