import time
import csv
import random

def MainMenu():
    print("Welcome to my quiz")
    print("This quiz will test your knowledge on <placeholder>")
    print("Would you like to login to the quiz?\n")
    time.sleep(1)

    choice = False
    while choice == False:
        menu = input("Would you like to login? (y/n) ")
        menu = menu.lower()

        if menu == "y":
            print("\nLogin activated")
            LogIn()
            choice = True
        elif menu == "n":
            print("Ok Bye")
            break
        else:
            print("Invalid Option")