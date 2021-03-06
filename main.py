from win32com.client import Dispatch
import random
from termcolor import cprint
from time import sleep


def game():

    chances = 0
    opp_win = 0
    user_win = 0

    while (chances != 10):

        adi = ['s', 'w', 'g']
        opp = random.choice(adi)

        user = input("Enter 's' for Snake, 'w' for Water and 'g' for Gun.\n")

        if user == opp:
            print("Oops!!\nMatch draw")
            sleep(1)
            print("You chooses", user, "And your opponent chooses", opp)
            chances += 1

        if user == 's' and opp == 'w':
            print("You chooses", user, "And your opponent chooses", opp)
            sleep(1)
            print("HURRAY!!")
            print("You win!")
            user_win += 1
            chances += 1
            sleep(1)

        elif user == 'w' and opp == 's':
            sleep(1)

            print("You Loose!")
            print("\t\tDont worry, try again.")
            print("You chooses", user, "And your opponent chooses", opp)
            sleep(1)

            chances += 1
            opp_win += 1

        if user == 'g' and opp == 'w':
            sleep(1)

            print("You Loose!!")
            print("\t\tDont worry, try again.")
            print("You chooses", user, "And your opponent chooses", opp)
            sleep(1)

            chances += 1
            opp_win += 1

        elif user == 'w' and opp == 'g':
            sleep(1)

            print("HURRAY!!")
            print("You win!")
            print("You chooses", user, "And your opponent chooses", opp)
            sleep(1)

            user_win += 1
            chances += 1

        if user == 's' and opp == 'g':

            print("You Loose!!")
            print("\t\tDont worry, try again.")
            print("You chooses", user, "And your opponent chooses", opp)
            chances += 1
            opp_win += 1

        elif user == 'g' and opp == 's':
            sleep(1)

            print("HURRAY!!")
            print("You win!")
            print("You chooses", user, "And your opponent chooses", opp)
            sleep(1)

            user_win += 1
            chances += 1
    sleep(1)
    print("Your final score is:-", user_win,
          "Your opponent score :-", opp_win)
    print("Hope you enjoyed!\nCome soon!!")
    again_play()


def again_play():

    play_again = input(
        "\t\t\tWant to play again?\nEnter 'y' for Yes and 'n' for No.\n")
    if play_again == 'y':
        sleep(1)
        game()
    elif play_again == 'n':
        sleep(1)
        print("\t\t*Thank You*!!\nCome Back Soon!")
    else:
        print("Wrong input.Please type 'y' or 'n' only.")
        sleep(1)
        again_play()


if __name__ == "__main__":
    adi = Dispatch("SAPI.spvoice")
    adi.speak("Welcome to snake water gun game")
    cprint("#" * 50, "magenta")
    cprint((f"SNAKE WATER GUN GAME ").center(50), "yellow")
    cprint("#" * 50, "magenta")
    sleep(1)
    print("WELCOME!")
    game()
