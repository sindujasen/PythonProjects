'''
THIS IS A ROCK PAPER SCISSOR GAME
ROCK = R - 1
PAPER = P - 2
SCISSOR = S - 3
'''

import random

def gameStarts():
    computerWins = 0
    userWins = 0
    chances = 5
    count = 0
    gamePar = {1: 'ROCK', 2: 'PAPER', 3: 'SCISSOR'}

    while(count < chances):
        count += 1
        '''Computer's Choice'''
        comp_choice = random.randint(1, 3)


        '''User's choice'''
        print("You have only {} chances totally".format(chances))
        print("Enter '1' for ROCK  --- '2' for PAPER --- '3' for SCISSOR")
        print("This is your {} chance".format(count))
        user_Choice = int(input())

        if(user_Choice <1 or user_Choice > 3):
            print("Wrong choice")
            count -= 1

        if(comp_choice != user_Choice):
            if(comp_choice == 1):
                if(user_Choice == 2):
                    userWins += 1
                elif(user_Choice == 3):
                    computerWins += 1
            if(comp_choice == 2):
                 if (user_Choice == 1):
                     computerWins += 1
                 elif (user_Choice == 3):
                     userWins += 1
            if (comp_choice == 3):
                if (user_Choice == 1):
                    userWins += 1
                elif (user_Choice == 2):
                    computerWins += 1
        else:
            print("No points----ITS A TIE")
            print("Play again if you have a chance")

        print("Computer choice was {}".format(comp_choice))

    print("Computer won {} times".format(computerWins))
    print("You won {} times".format(userWins))

    if(computerWins < userWins):
        print("YAHOO CONGRATS ---- YOU'VE WON")
    elif(computerWins > userWins):
        print("COMPUTER WON - BETTER LUCK NEXT TIME")
    else:
        print("ITS A TIE")
    print("Play again later")

if __name__  == "__main__":
    gameStarts()


