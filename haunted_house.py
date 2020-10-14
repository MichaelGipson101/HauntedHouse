import random

USER_LIFE_POINTS = 20
MONSTER_LIFE_POINTS = 10
health_potion = random.randint(1, 5)


def game_over():
    global USER_LIFE_POINTS
    print("You have died. Better luck in the afterlife!")
    response = input("Would you like to play again? (Type yes or no)?")
    if response == "yes":
        USER_LIFE_POINTS = 20
        enter_the_house()
    elif response == "no":
        print("Thank you for playing!")


def floor1_fight():
    global USER_LIFE_POINTS
    print("You are attacked by a crowd of Ghosts.")
    number_of_ghosts = random.randint(1, 5)
    for i in range(number_of_ghosts):
        print("Ghost number ", i, " attacks!")
        USER_LIFE_POINTS -= 1
    print("Life points have been reduced to ", USER_LIFE_POINTS)
    if USER_LIFE_POINTS <= 0:
        game_over()

    response = input("You see a chest in the corner. Will you open it? (Type yes or no)")
    if response == "yes":
        print("You find a bottle of mysterious red liquid. Drinking it recovers some of your life points.")
        USER_LIFE_POINTS += health_potion
        print("You recover ", health_potion, " life points.")
        print("Your life point total is now ", USER_LIFE_POINTS, ".")
        print(
            "You notice a hidden staircase behind a large painting within the room you are in. You proceed to the "
            "next floor.")
        enter_floor2()
    elif response == "no":
        print("You ignore the shiny chest in front of you and proceed to the next floor.")
        enter_floor2()


def final_fight():
    global USER_LIFE_POINTS
    global MONSTER_LIFE_POINTS
    print("The monster in front of you attacks.")
    monster = 1
    for i in range(monster):
        print("You are slashed by the Monster's claws, leaving a large red mark across your chest. It begins to bleed.")
        USER_LIFE_POINTS -= 5
    print("Life points have been reduced to ", USER_LIFE_POINTS)
    if USER_LIFE_POINTS <= 0:
        game_over()

    response = input("Will you fight back? (Type yes or no)?")
    if response == "yes":
        print("You flail your arms at the monster, attempting to hit it.")
        number_of_hits = random.randint(1, 5)
        for i in range(number_of_hits):
            print("You land a hit!")
            MONSTER_LIFE_POINTS -= 5
        print("The Monster's Life points have been reduced to ", MONSTER_LIFE_POINTS)
        if MONSTER_LIFE_POINTS <= 0:
            print(
                "Though you bested the monster in front of you, you don't notice a box behind you as you move away from the now-dead Monster."
                "\nTime slows to a halt as you lose your footing, tumbling through the glass window behind you.")
            victory()
    elif response == "no":
        print(
            "You remain frozen in place. The monster hesitates for only a moment before driving its claws into your chest.")
        game_over()


def enter_final_floor():
    print(
        "You enter the attic of the house. Most of the space is covered by boxes and other items. \nYou notice that the"
        "Monster is in the back of the room, but it has yet to notice you."
        "\nYou also notice that there is an open window on the other side of the room.")
    response = input(
        "Will you try to escape, or confront the monster who has been haunting you? (Type escape or fight)")
    while True:
        if response == "escape" or response == "fight":
            break
        else:
            print("Time passes as you ponder your decision.")
            response = input(
                "Will you try to escape, or confront the monster who has been haunting you? (Type escape or fight)")
            break

    if response == "escape":
        print(
            "You manage to find your way to the window without alerting the Monster. \nHowever, as you try to climb out,"
            "you slip. You let out a scream as you fall.")
        victory()
    if response == "fight":
        print(
            "The Monster stirs as you approach, coming to its feet with alarming speed. For a moment, it stares at you."
            "\nIt reaches out with its long, tendril-like claws to attack you.")
        final_fight()


def enter_floor9():
    pass


def enter_floor8():
    pass


def enter_floor7():
    pass


def floor_4():
    response = input(
        "You see two doors, one door becomes red, the other becomes blue. Pick the door you want to run too")
    while True:

        if response == "red" or response == "blue":
            break
        else:
            print("Select the valid door!")
            response = input(
                "You see two doors, one door becomes red, the other becomes blue. Pick the door you want to run too")
    if response == "red":
        enter_red_room()
    if response == "blue":
        enter_blue_room()


def enter_red_room():
    response = input(
        "You open the red door and see giant bats flying towards you, would you like to close the door or fight the bats?")
    while True:
        if response == "close" or response == "fight":
            break
        else:
            print(" Hey make sure to select either close or fight!")
            response = input(
                "You open the red door and see giant bats flying towards you, would you like to close the door or fight the bats?")
            break
    if response == "close":
        print(
            "you closed the door and stepped back, you realized you are trapped in this house and you will have to escape")
        floor_4()
    if response == "fight":
        attack_bats()


def attack_bats():
    print(" you pull out your sword and attack the bats, luckily you have armor so the bats did no damage to you")
    response = input(" you see that there is a mega bat that is flying towards you, do you want to fight or runaway?")
    while True:
        if response == "runaway" or response == "fight":
            break
        else:
            print("invalid answer try again")
            response = input(
                "you see that there is a mega bat that is flying towards you, do you want to (fight or runaway)?")
        break
    if response == "runaway":
        print(
            "You decided not to fight the mega bat and begin to run, the mega bat swoops in and grabs you by the head. Game Over")
        game_over()
    elif response == "fight":
        floor_5()


def floor_5():
    print(
        "The bat knocks you out and snatches you away, luckily you manage to drive your sword in its heart causing it to crash and drop you into a new area. \nYou decided to explore the area and see an ancient treasure")
    response = input("Do you want to open the treasure or move forward?")
    while True:
        if response == "open" or response == "move forward":
            break
        else:
            print("You think hard on your decision")
            response = input("Do you want to open the treasure or move forward? ( type open or move forward) ")
            break
    if response == "open":
        print("You open the treasure chest, a vine grabs on to you and drags you inside the chest.... you died")
        game_over()
    if response == "move forward":
        print(
            "You decided to explore the area and see a mysterious figure staring at you... \nYou decide to run to the nearest door and shut the door.")
        floor_6()


def enter_blue_room():
    print(
        "You entered the blue room you hear something screech, you turn around its a monster whos out for your blood. you begin to run")
    response = input("Will you run to the left or right?")
    while True:
        if response == "left" or response == "right":
            break
        else:
            print("You dont have much time!, you must run either left or right!")
            response = input("Do you want to open the treasure or move forward? ( type open or move forward) ")
            break
    if response == "left":
        print(
            "You decided to run left, you run through many rooms but the monster is catching up to you. \nYou jump into a vent and hide from the monster.You continue to move forward and see theres an empty hallway")
        response = input("Would you like to explore? (yes or no)")
        if response == "yes":
            floor_6()
        if response == "no":
            print("The monster breaks through the vent and captures you... Game over")
    if response == "right":
        print("You run into a dead end, the monster captures you and drags you to a dungeon")
        print(
            "You are locked up and cannot escape, you realize you have a knife in your pocket and crave your way through the door.")
        enter_floor2()


def floor_6():
    print(
        "You began exploring the area and see writing on the door which says: \nIf you get lost in the middle of nowhere And come across this place in the night, \nthink twice about knocking on their front door Unless you want to get a big fright ")
    response = input("You now see the door glowing, would you like to open the door?")
    while True:
        if response == "yes" or response == "no":
            break
        else:
            print("Listen you have no time right now! select yes or no to proceed, if you want to live.")
        response = input("You now see the door glowing, would you like to open the door?")
        break
    if response == "yes":
        print(
            "You open the glowing door and see a huge figure staring at you, he raises his fingers pointing at you. You realize that writing has a meaning."
            "You knock on the door twice and the figure disappears. You continue to move forward  ")
        enter_floor7()
    if response == "no":
        print(
            "The monster appears from behind and knocks you out, you wake up couple mins in a small room which is locked."
            "You search through the entire room and see a small door on the side. You open the door and it teleports you somewhere.")
        enter_floor7()


def floor_3_left():
    global USER_LIFE_POINTS
    print(
        "You struggle to fit through the small opening. It is damp, and you flinch as bugs and spiders skitter around you."
        "\nYou eventually find yourself in a small room, with a large vest laying on the floor in front of you.")
    response = input("We see a chest in the corner! Should we open it (Type yes or no)?")
    if response == "yes":
        print(
            "You put the vest on. Though it weighs down on you, you feel as if you could take a few more hits than usual.")
        USER_LIFE_POINTS += 10
        print("You gain an additional 10 Life Points.")
        print("Your life point total is now ", USER_LIFE_POINTS, ".")
        print("You see a ladder leading up to the next floor.")
        floor_4()
    elif response == "no":
        print(
            "You ignore the vest, thinking that the extra weight would slow you down. Instead, you see a ladder leading up to the next floor.")
        floor_4()


def enter_bonus_floor():
    global USER_LIFE_POINTS
    print("You hit a concrete floor below you, twisting your ankle in the process.")
    USER_LIFE_POINTS -= 7
    print("Your life point total is now ", USER_LIFE_POINTS, ".")
    print("After the pain subsides, you notice that there is a large spiral staircase in the corner of the room."
          "\n There is also a door to your left leading somewhere else.")
    response = input(
        "Which staircase will you take? (Type forward or left)")
    while True:
        if response == "forward" or response == "left":
            break
        else:
            print("Time passes as you ponder your decision.")
            response = input(
                "Which staircase will you take? (Type forward or left)")
            break

    if response == "forward":
        print("The spiral staircase takes you much farther up into the house than you would have expected."
              "\nYou find yourself on a new floor.")
        floor_5()
    if response == "left":
        print("The staircase to your left takes you to an unfamiliar hallway above where you were before.")
        floor_4()


def floor_3_forward():
    print("You enter a large bedroom, presumably for whoever lived in the house before it was abandoned.\n"
          "The room stinks of perfume, an odd scent for a place long since abandoned."
          "\nAs you approach the bed at the center of the room, you step on a loose floorboard. You fall through the floor.")
    enter_bonus_floor()


def enter_floor3():
    print(
        "You enter a large, dark room. There is nothing inside except for a lone wooden chair, and a spotlight above it."
        "\nYou notice that there is a large wooden door in front of you, and a small crawl space to your left. Which will you choose?")
    response = input(
        "Will you take the door in front of you, or try your hand in the crawl space? (Type forward or left)")
    while True:
        if response == "forward" or response == "left":
            break
        else:
            print("Time passes as you ponder your decision.")
            response = input(
                "Will you take the door in front of you, or try your hand in the crawl space? (Type forward or left)")
            break

    if response == "forward":
        floor_3_forward()
    if response == "left":
        floor_3_left()


def floor2_fight():
    global USER_LIFE_POINTS
    print("You are attacked by a crowd of Ghosts.")
    number_of_ghosts = random.randint(1, 5)
    for i in range(number_of_ghosts):
        print("Ghost number ", i, " attacks!")
        USER_LIFE_POINTS -= 1
    print("Life points have been reduced to ", USER_LIFE_POINTS)
    if USER_LIFE_POINTS <= 0:
        game_over()

    response = input("You see a chest in the corner. Will you open it? (Type yes or no)")
    if response == "yes":
        print("You find a bottle of mysterious red liquid. Drinking it recovers some of your life points.")
        USER_LIFE_POINTS += health_potion
        print("You recover ", health_potion, " life points.")
        print("Your life point total is now ", USER_LIFE_POINTS, ".")
        print("You enter the hallway again, noting that the scratching seems to have stopped. At least for now.")
        enter_floor3()
    elif response == "no":
        print("You ignore the shiny chest in front of you and find yourself back in the hall from which you came.")
        enter_floor2()


def enter_floor1_left():
    response = input(
        "You find some ghosts who are attacking you! What do you do: run away or fight? (Type fight or run away)")
    if response == "fight":
        floor1_fight()
    elif response == "run away":
        print("You run back the way you came, finding yourself back at the beginning.")
        enter_the_house()


def floor2_death():
    global USER_LIFE_POINTS
    print("As you find yourself lost in the darkness, you begin to notice heavy breathing behind you. \n"
          "Your heart rate slows to a crawl as you find yourself unable to turn around. You lose consciousness as "
          "long, thin fingers wrap themselves around your neck. \n "
          "You find yourself within a dream that you will never wake up from.")
    USER_LIFE_POINTS -= 500

    if USER_LIFE_POINTS <= 0:
        game_over()


def enter_floor2_right():
    response = input(
        "You encounter a group of Ghosts huddled around a small table. Will you Fight or Run Away? (Type fight or run "
        "away)")
    if response == "fight":
        floor2_fight()
    elif response == "run away":
        print("You run back the way you came, finding yourself back to where you were before.")
        enter_floor2()


def floor2_continue():
    print("The scratching is almost deafening at this point. Will you keep going, or will you hide?")
    response = input(
        "You see a door on your left that may offer you a hiding place. (Type proceed or hide)")
    while True:
        if response == "proceed" or response == "hide":
            break
        else:
            print("Time passes as you ponder your decision.")
            response = input("You see a door on your left that may offer you a hiding place. (Type proceed or hide)")
            break

    if response == "proceed":
        print(
            "You press deeper into the darkness, the scratching becoming unbearable as you panic, trying to figure "
            "out where the noise is coming from.")
        floor2_death()
    if response == "hide":
        print(
            "You struggle to stay quiet as your heart beats in your chest. The scratching noise moves down the "
            "hallway, passing by the room you are in. \n "
            "You catch a glimpse of the hideous monster you almost fell victim to, sending a shiver down your spine. "
            "\nYou wait until the noise subsides and continue deeper into the house.")
        enter_floor3()


def enter_floor2():
    print("You enter a long hallway, lights flickering dimly throughout the long hall. "
          "\n You hear a slow, methodical scraping noise from the darkness at the end of the hall.")
    response = input(
        "You see a door on your right. Will you open it, or will you proceed down the hallway? (Type proceed or right)")
    while True:
        if response == "proceed" or response == "right":
            break
        else:
            print("Time passes as you ponder your decision.")
            response = input(
                "You see a door on your right. Will you open it, or will you proceed down the hallway? (Type proceed or right)")
            break

    if response == "proceed":
        print("You press deeper into the darkness, the scratching becoming clearer and clearer the farther you go.")
        floor2_continue()
    if response == "right":
        enter_floor2_right()


def enter_floor1_right():
    global USER_LIFE_POINTS
    print(
        "You open the large wooden door to your right. You make your way up the broken staircase, wincing as you step "
        "on a nail. You lose 3 life points.")
    USER_LIFE_POINTS -= 3
    print("Your life point total is now ", USER_LIFE_POINTS, ".")
    enter_floor2()


def enter_the_house():
    print("You approach a Haunted House. The night creeps up upon you as you enter.")
    response = input(
        "Once inside, the door behind you locks. You will have to advance through the house to escape."
        "\nIn front of you, there are two doors. One to the left, and one to your right. Which one will you open? (Type right "
        "or left)")
    while True:
        if response == "left" or response == "right":
            break
        else:
            print("Time passes as you ponder your decision.")
            response = input(
                "Two doors remain on your left and your right as rain begins to fall outside. Which will you choose? "
                "(Type right or left)")
            break
    if response == "left":
        enter_floor1_left()
    if response == "right":
        enter_floor1_right()


def play_again():
    global USER_LIFE_POINTS
    print("You have survived your night in the Haunted House. Congratulations on living to tell the tale!")
    response = input("Would you like to play again? (Type yes or no)?")
    if response == "yes":
        USER_LIFE_POINTS = 20
        enter_the_house()
    elif response == "no":
        print("Thank you for playing!")


def victory():
    global USER_LIFE_POINTS
    print("You fall for what seems like hours, falling from the 10th floor all the way down to the ground. \nYou "
          "groan in pain as the grass beneath you cushions your fall.")
    print("\n You look back up at the house above, a pair of beady red eyes peering back from the window you just "
          "fell from. \nYou wince as a stinging pain engulfs your abdomen.")
    USER_LIFE_POINTS -= 7

    if USER_LIFE_POINTS <= 0:
        game_over()
    else:
        print("The pain is a temporary feeling, as the adrenaline pumping through your veins gets you to your feet - "
              "and far away from the house you just escaped.")
        play_again()


def run():
    enter_the_house()
