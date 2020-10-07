import random

USER_LIFE_POINTS = 20


def fight_ghosts():
    global USER_LIFE_POINTS
    print("The ghosts are attacking us!!!!")
    number_of_ghosts = random.randint(1, 5)
    for i in range(number_of_ghosts):
        print("Ghost number ", i, " attacked us!")
        USER_LIFE_POINTS -= 1
    print("Life points have been reduced to ", USER_LIFE_POINTS)
    response = input("We see a chest in th corner! Should we open it (yes or no)?")
    if response == "yes":
        pass
    elif response == "no":
        pass


def enter_left_room():
    response = input("You find some ghosts who are attacking you! What do you do: run away or fight?")
    if response == "fight":
        fight_ghosts()
    elif response == "run away":
        enter_the_house()


def enter_right_room():
    pass


def enter_the_house():
    print("Welcome to the haunted house!")
    response = input("You see two doors, one to the left, and one to your right! Which one do you want to open?")
    while True:
        if response == "left" or response == "right":
            break
        else:
            print("Enter a valid room!")
    response = input("You see two doors, one to the left, and one to your right! Which one do you want to open?")
    if response == "left":
        enter_left_room()
    if response == "right":
        enter_right_room()


def run():
    enter_the_house()
