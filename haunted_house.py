import random

USER_LIFE_POINTS = 20


def game_over():
    print("You have died. Better luck in the afterlife!")


def fight_ghosts():
    global USER_LIFE_POINTS
    print("The ghosts are attacking us!!!!")
    number_of_ghosts = random.randint(1, 5)
    for i in range(number_of_ghosts):
        print("Ghost number ", i, " attacked us!")
        USER_LIFE_POINTS -= 1
    print("Life points have been reduced to ", USER_LIFE_POINTS)
    if USER_LIFE_POINTS <= 0:
        game_over()

    response = input("We see a chest in th corner! Should we open it (yes or no)?")
    if response == "yes":
        pass
    elif response == "no":
        pass


def enter_room1_left():
    response = input("You find some ghosts who are attacking you! What do you do: run away or fight?")
    if response == "fight":
        fight_ghosts()
    elif response == "run away":
        print("You run back the way you came, finding yourself back at the beginning.")
        enter_the_house()


def hall1_death():
    global USER_LIFE_POINTS
    print("As you find yourself lost in the darkness, you begin to notice heavy breathing behind you. /n"
          "Your heart rate slows to a crawl as you find yourself unable to turn around. You lose consciousness as long, thin fingers wrap themselves around your neck. /n"
          "You find yourself within a dream that you will never wake up from.")
    USER_LIFE_POINTS -= 500

    if USER_LIFE_POINTS <= 0:
        game_over()


def enter_room2_right():
    pass


def enter_room2():
    print("You enter a long hallway, lights flickering dimly throughout the long hall. "
          "/n You hear a slow, methodical scraping noise from the darkness at the end of the hall.")
    response = input("You see a door on your right. Will you open it, or will you proceed down the hallway?")
    while True:
        if response == "proceed" or response == "right":
            break
        else:
            print("Time passes as you ponder your decision.")
            response = input("You see a door on your right. Will you open it, or will you proceed down the hallway?")
            break

    if response == "proceed":
        print("You press deeper into the darkness, the scratching becoming clearer and clearer the farther you go.")
        hall1_death()
    if response == "right":
        enter_room2_right()


def enter_room1_right():
    enter_room2()


def enter_the_house():
    print("You approach a Haunted House. The night creeps up upon you as you enter.")
    response = input("Once inside, you see two doors. One to the left, and one to your right. Which one will you open?")
    while True:
        if response == "left" or response == "right":
            break
        else:
            print("Time passes as you ponder your decision.")
            response = input(
                "Two doors remain on your left and your right as rain begins to fall outside. Which will you choose?")
            break
    if response == "left":
        enter_room1_left()
    if response == "right":
        enter_room1_right()


def run():
    enter_the_house()
