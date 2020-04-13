'''
Password Generator
digits = {0,1,2,3,4,5,6,7,8,9}
alphabets (lowercase and uppercase) = {a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z}
symbols = {_,@,!,&,*}
'''
import random

def password_gen():
    masterlist = []
    digitSub = []
    lowerSub = []
    upperSub = []
    symbolSub = []
    password = ""

    digits = ['0','1','2','3','4','5','6','7','8','9']
    lowerCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    symbols = ['_', '@', '!', '&', '*']
    upperCase = []

    for alpha in lowerCase:
        letter = alpha.upper()
        upperCase.append(letter)

    print("How many digits you want to be in your password")
    digitNum = int(input())

    for item in list(range(0,digitNum)):
        choice = random.choice(digits)
        digitSub.append(choice)
    masterlist.extend(digitSub)


    print("How many lowercase letters you want to be in your password")
    lowerNum = int(input())

    for item in list(range(0,lowerNum)):
        choice = random.choice(lowerCase)
        lowerSub.append(choice)
    masterlist.extend(lowerSub)


    print("How many uppercase letters you want to be in your password")
    upperNum = int(input())

    for item in list(range(0,upperNum)):
        choice = random.choice(upperCase)
        upperSub.append(choice)
    masterlist.extend(upperSub)


    print("How many symbols you want to be in your password")
    symbNum = int(input())
    
    for item in list(range(0,symbNum)):
        choice = random.choice(symbols)
        symbolSub.append(choice)
    masterlist.extend(symbolSub)

    if(len(masterlist) > 6):
        random.shuffle(masterlist)
        password = "".join(masterlist)
        print("Your password is {}".format(password))
    else:
        print("It should be more than 6---GENERATE ONCE AGAIN")
        exit()











if __name__  == "__main__":
    print("PASSWORD GENERATOR")
    print("******************\n")
    print("You can use digits(0-9, alphabets(uppercase and lowercase) and symbols{_,@,!,&,*}\nIt should be more than 6")
    password_gen()



