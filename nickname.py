#Ivan
#nickname generator
# asks the user a series of questions to see what their band would be

print("Welcome to the band rec geneterator!")

#post hardcore
genre = input("Which do you prefer post-hardcore or pop-punk: ")
if genre == "post-hardcore":
    popularity = input("more known or less known: ")
    if popularity == "more known":
        haircut = input("bob or no bob: ")
        if haircut == "no bob":
            print("Your band is ptv!")
        else:
            print("your band is sws!")
    else:
        if popularity == "less known":
            sad = input("hella sad or not hella sad: ")
            if sad == "hella sad":
                print("Your band is La Dispute!")
            else:
                print("Your band is Picture Me Broken!")


#pop punk
else:
    if genre == "pop-punk":
        age = input("older band or newer band: ")
        if age == "older band":
            lead = input("male lead or female lead: ")
            if lead == "male lead":
                print("Your band is Panic! At The Disco!")
            else:
                print("your band is Paramore!")

        else:
            if age == "newer band":
                sound = input("more of a traditional sound or more of a midwest emo sound: ")
            if sound == "more of a traditional sound":
                print("Your band is Neck Deep!")
            else:
                print("your band is Hot Mulligan!")


