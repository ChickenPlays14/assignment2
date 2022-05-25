import time
import csv
import random


def MainMenu():
    print("Welcome to my quiz")
    print("This quiz will test your knowledge on cities")
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


def LogIn():
    password = "city"
    choice = False
    while choice == False:
        user = input("Please enter the password: ")
        if user == password:
            print("\nPassword correct, good luck with the quiz!")
            quiz()
            choice = True

        else:
            print("Password Incorrect")


def quiz():
    global score
    score = 0
    chances = 1
    print("You will have", chances, "chance to answer correctly. \nPlease make sure to answer the question correctly\n")
    time.sleep(2)

    original_questions = [
        ["Which city is the capital of England?", "London"],
        ["Which city is the capital of Portugal?", "Lisbon"],
        ["Which country is Hamburg located in?", "Germany"],
        ["Which country is Bologna located in?", "Italy"],
        ["Which American state is the city of Nashville located in?", "Tennessee"],
        ["Which American state is the city of Albuquerque located in?", "New Mexico"],
        ["Which country is Havana located in?", "Cuba"],
        ["Which City used to be called Constantinople", "Istanbul"]
    ]

    random_order = []
    while len(original_questions) > 0:
        question = random.randint(0, len(original_questions) - 1)
        random_order.append(original_questions[question])
        original_questions.pop(question)

    for x in random_order:
        print(x[0])
        answer = input("What is your answer? ")
        if answer == x[1]:
            print("Correct!")
            score += 1

        else:
            print("Incorrect!")


def highscores():
    scores = []
    names = []
    results = []

    with open ("playerscore.csv", mode = "r") as myfile:
        for each in myfile:
            each = each.rstrip("\n")

            scores.append(each)


    for each in scores:
        each = each.split(",")
        name = each[0]
        result = each[1]
        names.append(name)
        results.append(result)


    highest = 0
    high_scores = []

    for count in range(5):
        highest = 0

        for each in results:
            if int(each) > highest:
                highest = int(each)
                index_number = results.index(each)

        high_scores.append(str(highest) + "" + names [index_number])
        results.pop(index_number)
        names.pop(index_number)

    print(high_scores)
    print("Thank you for completing the quiz!")


MainMenu()

while score >= 4:
    print("Well done! Your score was", score)
    break

while score <= 3:
    print("Better luck next time! Your score was", score)
    break

print("You scored", score, "points!")
username = input("Please enter your name for our leaderboard: ")
print("\n")

print("Thank you for playing the city quiz!")

entry = username + ", " + str(score)

score = []

with open ("playerscore.csv", mode = "r") as Myfile:

    for each in Myfile:
        each = each.rstrip("\n")
        score.append(each)

score.append(entry)


with open ("playerscore.csv", mode = "w") as Myfile:
    for each in score:
        Myfile.write(each + "\n")

highscores()