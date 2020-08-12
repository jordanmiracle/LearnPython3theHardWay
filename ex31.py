#  Print what the scenario is
print("""You enter a dark room with two doors.  
Do you go through door #1 or door #2?""")
#  Prompt the user for input
door = input("> ")

if door == '1':
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off.")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, beginsdoing {bear} is probably better.")
        print("Bear runs away.")
elif door == "2":
    print("You stare into the endless abyss at Cthulu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")
else:
    print("You stumble around and fall on a knife and die. Good job!")

    print("""You walk out of your door and see a bright light in the sky. 
    It is quiet, but seems to be slowly hovering toward you. 
    Do you walk toward it to investigate, or turn around a run inside?""")

    light = input(" >")

if light == "1":
    print("The light starts to pulsate a little bit, and it seems to be coming even lower. You are slightly scared, but even more curious.")
    print("What do you do?")
    print("1. Get frightened and call for somebody.")
    print("2. Slowly walk toward the light.")

    action = input("> ")
    
if action == "1":
    print("The light starts to pulsate and you begin to feel a sense of calm.")
elif action == "2":
    print("The light retreats a little ways and starts to dim.")
else:
    print("The light retreats almost instantly off to the West.")

if light == "2":
    print("You start to hear a light buzzing noise that seems to be coming from all around you.")
    print("What do you do?")
    print("1. You go hide in your bed under the blankets.")
    print("2. You go back outside to see if the buzzing stops.")

    buzzing = input("> ")

    if buzzing == "1":
        print("""Your eyes quickly start to get heavy and you drift off into what seems 
        like a very light sleep, yet you have the strangest dreams...""")
    elif buzzing == "2":
        print("The buzzing does seem to slowly wane, the light brightens a bit and starts moving slowly downward...")


else:
    print("The light disappears almost instantly off to the East.")

