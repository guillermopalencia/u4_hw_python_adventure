# Create your own adventure with python here
name = input("Enter Your Name: ")

if name:
    print("Hello " + name, "Would you like to start an adventure to find the ultimate treasure and live a life of riches and jewels?")
    choice1 = input("Yes or No?: ")
    if choice1 == "Yes":
        print("Okay, Choose a weapon")
        print("Sword, Gun, or Shield")
    elif choice1 == "No":
        print("How unfortunate")
    choice2 = input(":")
    if choice2 == "Sword" or choice2 == "Gun":
        print("Wise choice")
        print("pick a path to continue on your journey. Do you wish to travel via Sky, Land, or Sea?")
    elif choice2 == "Shield":
        print("You pick up the shield and notice a red gem on the floor, you pick it up")
        print("pick a path to continue on your journey. Do you wish to travel via Sky, Land, or Sea?")
    choice3 = input(":")
    if choice3 == "Sky":
        print("You enter a plane and travel to Mount Hagard.")
        print("You land on the beach south side of the Mountain, prepare for a hike.")
        print("Do you wish to take a more risky 30 minute hike or the safe 2 hour hike.")
        choice1 = input("Short or Long:")
        if choice1 == "Short":
            print("You take the short Trail up the mountain")
            print("While ascending the Mountain you discover a small crack in the Wall just big enough to squeeze in")
            print(
                "While peaking inside you see a glowing yellow light. Do you enter the crack?")
            choice = input("Enter? Yes or No:")
            if choice == "Yes":
                print("You enter the crack")
                print(
                    "While squeezing through you realize theres is no longer footing and you fall inside.")
                print(
                    "You fall and land on a pile of gold, breaking your leg. You are unfazed by your injury out of joy.")
                print(
                    "You soon realize there's no way to exit. You eventually die surrounded by riches.")
        elif choice1 == "Long":
            print("You Ascend the Mountain taking the longer hike / path.")
            print("You reach the end of the trail just below the Peak and discover a cave with a riddle and a lever.")
            print("You realize the lever will not work until the riddle is solved")
            print("A metal neither black nor red, As heavy as mans golden greed. What you do to stay ahead, With friend or foe or arrow and steed.")
            answer = input("What am I? :")
            if answer == "Lead" or answer == "lead":
                print("You pull the lever and open a secret passage")
                print("Congrats you found Hagards Treasure")
            else:
                print("You pull the lever")
                print(
                    "You hear a loud noise before the floor below you pulls away landing on a spike trap")
                print(
                    "You land on the spikes and look around to see the writing Lead to Greed on the walls")
                print(
                    "Unfortunately this is where your journey ends and you do not find the Treasure.")
    elif choice3 == "Sea":
        print("You Board a speed boat and travel to Mount Hagard.")
        print("You land on the beach North of the Mountain, prepare for a hike.")
        print("Do you wish to take a more risky 30 minute hike or the safe 2 hour hike.")
        choice1 = input("Short or Long:")
        if choice1 == "Short":
            print("You travel up the short trail to the Mountain")
            print("As you are hiking you see a warning sign")
            print("Fools will follow their greed to a Treasure that is not theirs")
            print("Do you adhere to the warning and turn back?")
            choice = input("Yes or No?:")
            if choice == "Yes":
                print("You turn back to the beach and return home where you came from")
                print("You leave the island with your life")
            elif choice == "No":
                print("You continue hiking ignoring th warning")
                print("You discover an opening in the mountain filled with goal")
                print("You enter the room only to immediately have it be blocked off")
                print(
                    "You plead in your head as the room slowly fills with sand leaving you stuck with your Greed till you die")
        elif choice1 == "Long":
            print("You Ascend the Mountain taking the longer hike / path.")
            print("You reach the end of the trail just below the Peak and discover a cave with a riddle and a lever.")
            print("You realize the lever will not work until the riddle is solved")
            print("A metal neither black nor red, As heavy as mans golden greed. What you do to stay ahead, With friend or foe or arrow and steed.")
            answer = input("What am I? :")
            if answer == "Lead" or answer == "lead":
                print("You pull the lever and open a secret passage")
                print("Congrats you found Hagards Treasure")
            else:
                print("You pull the lever")
                print(
                    "You hear a loud noise before the floor below you pulls away landing on a spike trap")
                print(
                    "You land on the spikes and look around to see the writing Lead to Greed on the walls")
                print(
                    "Unfortunately this is where your journey ends and you do not find the Treasure.")
    elif choice3 == "Land":
        print("You enter a tesla model x and travel to Mount Hagard.")
        print(
            "Along the way the path is blocked, but there is a horse nearby. Lucky you :)")
        print("With the horse you arrive at the base of Mount Hagard, Luckily you have a horse and can now safely travel up.")
        print("Your path leads you to a cave. You can enter the cave or continue the path up the mountain.")
        choice = input("Enter Cave? Yes/No:")
        if choice == "Yes":
            print(
                "You enter the cave and discover a mysterious rock with engravings in it.")
            print("You notice a small opening in the center of the rock and decide to place the gemstone you had in it.")
            print("The rock rises slowly revealing a letter from Hagard! You've discovered his treasure you're rich now congrats!")
        elif choice == "No":
            print("You continue up the mountain.")
            print("An eagle swoops down and snatches your red gemsone.")
            print(
                "You arrive at the peak of Mt Hagard to find an opening that decends downward.")
            print(
                "While descending into the opening you slip, falling to your doom. Game Over :(")
