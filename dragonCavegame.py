import random
import time

#we will create own functions, so we can simply call the code and not
#have to keep writing same code over and over

def displayIntro():
    print("You are in a land full of dragons.")
    time.sleep(2) # time unit in seconds
    print ('''In front of you, you see two caves. In one cave,
the dragon is frendly and will share his treasure with you.
The other dragon is greedy and hungry and will eat you on sight''','\n')

def chooseCave():
    cave = ''
    while cave !='1' and cave !='2':
        print("Which cave will you go into?(1 or 2)")
        cave = input()

    return cave

def checkCave(chooseCave):
    print("You apprach the cave...")
    time.sleep(2)
    print("It is dark and spooky...")
    time.sleep(2)
    print("A large dragon jumps out infront of you! He opens his jaws and ...")
    print()
    time.sleep(2)

    friendlyCave = random.randint(1,2)

    if chooseCave == str(friendlyCave):
        print("Give you hus treasure!")

    else:
        print("Gobbles you down in one bite!")


playAgain ='yes'
while playAgain =="yes" or playAgain =='y':
    displayIntro()

    caveNumber = chooseCave()

    checkCave(caveNumber)

    print("Do you want to play again? (yes or no)")
    playAgain = input()
