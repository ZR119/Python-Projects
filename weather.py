#Ivan
#weather
#program that tells you what clothes to wear depending on the weather

def weather():
    temperature = int(input("whats the temperature outside: "))
    if temperature >= 70 :
        print("wear light clothing")
    elif temperature >= 40:
        print("wear alot of layers")
    else:
        print("stay indoors")

weather()
