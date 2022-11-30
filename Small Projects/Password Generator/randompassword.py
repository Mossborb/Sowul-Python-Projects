#Creates a random password after selecting length 
#TODO: Needs to be readjusted, inputing 5 creates a password length of 6
import random

def clear():
    print("\n" * 100)

aLetter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
aNumber = "1234567890"
aSymbol = "!@#$%^&*"


def createPassword(length):
    password = []
    count = 0

    while True:
        if count > length:
            break
        
        #Sets a random number in the range of the strings aLetter, aNumber, aSymbol
        randomLetter = random.randrange(0,52) #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
        randomNumber = random.randrange(0,10) #1234567890
        randomSymbol = random.randrange(0,8)  #!@#$%^&*
        
        #Picks a random character, from the randomly selected 
        pickRandom = [aLetter[randomLetter],aNumber[randomNumber],aSymbol[randomSymbol]]

        n = random.randrange(0,3)

        password.append(pickRandom[n])
        count += 1

    return ''.join(password)

def createWeakPassword(length):
    password = []
    count = 0

    while True:
        if count > length:
            break

        randomLetter = random.randrange(0,52)
        password.append(aLetter[randomLetter])

        count += 1
    
    return ''.join(password)

createPassword(5)

