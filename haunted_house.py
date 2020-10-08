import random

USER_LIFE_POINTS = 20
health_potion = random.randint(1, 5)


def game_over():
    print("You have died. Better luck in the afterlife!")


def floor1_fight():
    global USER_LIFE_POINTS
    print("You are attacked by a crowd of Ghosts.")
    number_of_ghosts = random.randint(1, 5)
    for i in range(number_of_ghosts):
        print("Ghost number ", i, " attacked us!")
        USER_LIFE_POINTS -= 1
    print("Life points have been reduced to ", USER_LIFE_POINTS)
    if USER_LIFE_POINTS <= 0:
        game_over()

    response = input("We see a chest in the corner! Should we open it (Type yes or no)?")
    if response == "yes":
        print("You find a bottle of mysterious red liquid. Drinking it recovers some of your life points.")
        USER_LIFE_POINTS += health_potion
        print("You recover ", health_potion, " life points.")
        print("Your life point total is now ", USER_LIFE_POINTS, ".")
    elif response == "no":
        print("You ignore the shiny chest in front of you and proceed to the next floor.")
        enter_floor2()


def enter_floor3():
    pass


def floor2_fight():
    global USER_LIFE_POINTS
    print("You are attacked by a crowd of Ghosts.")
    number_of_ghosts = random.randint(1, 5)
    for i in range(number_of_ghosts):
        print("Ghost number ", i, " attacked us!")
        USER_LIFE_POINTS -= 1
    print("Life points have been reduced to ", USER_LIFE_POINTS)
    if USER_LIFE_POINTS <= 0:
        game_over()

    response = input("We see a chest in the corner! Should we open it (Type yes or no)?")
    if response == "yes":
        print("You find a bottle of mysterious red liquid. Drinking it recovers some of your life points.")
        USER_LIFE_POINTS += health_potion
        print("You recover ", health_potion, " life points.")
        print("Your life point total is now ", USER_LIFE_POINTS, ".")
    elif response == "no":
        print("You ignore the shiny chest in front of you and proceed to the next floor.")
        enter_floor3()


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
          "Your heart rate slows to a crawl as you find yourself unable to turn around. You lose consciousness as long, thin fingers wrap themselves around your neck. \n"
          "You find yourself within a dream that you will never wake up from.")
    USER_LIFE_POINTS -= 500

    if USER_LIFE_POINTS <= 0:
        game_over()


def enter_floor2_right():
    response = input(
        "You encounter a group of Ghosts huddled around a small table. Will you Fight or Run Away? (Type fight or run away)")
    if response == "fight":
        floor2_fight()
    elif response == "run away":
        print("You run back the way you came, finding yourself back to where you were before.")
        enter_floor2()


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
            response = input("You see a door on your right. Will you open it, or will you proceed down the hallway?")
            break

    if response == "proceed":
        print("You press deeper into the darkness, the scratching becoming clearer and clearer the farther you go.")
        floor2_death()
    if response == "right":
        enter_floor2_right()


def enter_floor1_right():
    enter_floor2()


def enter_the_house():
    print("You approach a Haunted House. The night creeps up upon you as you enter.")
    response = input(
        "Once inside, you see two doors. One to the left, and one to your right. Which one will you open? (Type right or left)")
    while True:
        if response == "left" or response == "right":
            break
        else:
            print("Time passes as you ponder your decision.")
            response = input(
                "Two doors remain on your left and your right as rain begins to fall outside. Which will you choose? (Type right or left)")
            break
    if response == "left":
        enter_floor1_left()
    if response == "right":
        enter_floor1_right()


def run():
    enter_the_house()
