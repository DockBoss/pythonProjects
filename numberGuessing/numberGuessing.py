## importing dependencies
import random
import time

##prompt user to select which number game they want to play
print("Please select what game you want to play:\n1: number guessing\n2: guessing a number")

selection = int(input())

if selection == 1:

    ## generate number set state variable
    num = random.randint(0,100)
    correct = False
    count = 0
    ##prompt user
    print("guess the number correct and you win!")

    print(num)

    while correct != True:

        count += 1
        guess = int(input())
        
        if guess == num:
            correct = True
            print("You Won in: " + str(count) + " tries!")
        elif guess < num :
            print("Wrong, too low guess again!")
        else:
            print("Wrong, too high guess again!")

else:
    print("Pick a number between 0 and 100")
    time.sleep(10)
    print("Are you ready?")
    correct = False
    count = 0
    while correct != True:
        count += 1
        randGuess = random.randint(0,100)
        print('Is your number:' + str(randGuess))
        print("Y/N")
        response = input()
        if response == 'Y' or response == 'y':
            print("I won in " + str(count) + " tries!")
            correct = True
        else:
            print("I will get it right next time")
