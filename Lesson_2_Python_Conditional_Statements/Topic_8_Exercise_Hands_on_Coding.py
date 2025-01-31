weather_today = "Is Sunny"
user_name = input("Hello!, Whats your name?: ")
print(f"Hi {user_name} nice to meet you!")
user_mood = input (f"So, {user_name}! What mood are you in today? Sad/Happy: ") 
if user_mood == "Happy" and weather_today == "Is Sunny":
    print(f"{user_name} I recommend a Romantic movie!")
    if user_mood == "Happy" and weather_today == "Is Not Sunny":
        print(f"{user_name} I recommend watching a Comedy movie!")
        if user_mood == "Sad" and weather_today == "Is Not Sunny" or "Is Sunny":
                    print(f"{user_name} I recommend watching a Drama movie!")
        else:
               print(f"{user_name} I recommend a Adventure movie!")

temperature = int(input("What is today's tempature outside in Celsius?: "))
type_of_event = input("What type of event are you attending?: ")
if temperature <= 60:
      print(f"Today's is {temperature} Celsius?")
      if type_of_event == "Casual":
             print("Dress in somthing warm")