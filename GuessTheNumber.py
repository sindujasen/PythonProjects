import random

"""Generates  RANDOM NUMBER"""

actNumber = random.randint(0,20)
'''print("{}".format(actNumber))'''
ret = 0
count = 0

def guessFunc(actNumber, guessNum):
    if(guessNum != actNumber):
        if(guessNum < actNumber):
            print("Guess is too low")
            return (0)
        else:
            print("Guess is too high")
            return (0)
    else:
        print("Yahoo!!!! You are right .... The number is {}".format(actNumber))
        return(1)




while(ret != 1):
    count += 1
    chances  = 5
    if(count <= chances):
        print("Total chances are only {}".format(chances))
        print("You're in chance {} - Guess any number between 0 and 20 inclusive".format(count))
        guessNum = int(input())
        if(guessNum < 0 or guessNum > 20):
            print("Enter any number between 0 and 20 inclusive")
            break;
        else:
            ret = guessFunc(actNumber, guessNum)
    else:
        print("Game over ....You are done")
        break












