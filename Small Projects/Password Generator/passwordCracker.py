#Write a brute force method to check if password is correct. 

import randompassword as rpw
rpw.clear()


Password = rpw.createWeakPassword(2)
print(Password)

#Unknown length, so will have to iterate through alphbet starting with a-z, A-Z 

#If password has not been guessed create new slot, iterate through first, then second slot, keep adding 
#slots until password is guessed. 

#Iterate through a-z, A-Z

Letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" #52 in length
crackedPassword = []
i = 0
slot = 0
while True:
    #If list is empty, create a placeholder. 
    if len(crackedPassword) == 0:
        crackedPassword.append('a')

    #Iterate through 0th slot
    crackedPassword[slot] = Letters[i]
    if crackedPassword[slot] 
    #Once at end reset,


    # Check to see if password is correct
    if ''.join(crackedPassword) == Password:
        break



