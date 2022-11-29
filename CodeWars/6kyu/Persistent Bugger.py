#Learned how to multiply all ints in a list.


"""
Write a function, persistence, that takes in a positive parameter num and 
returns its multiplicative persistence, which is the number of times you must 
multiply the digits in num until you reach a single digit.
"""

#999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
import math
def persistence(n):
    iteration = 0
    while True:
        #take the number and split it into it's single digits
        #n = 999
        n = str(n)
        listOfNumbers = []
        for i in n:
            listOfNumbers.append(int(i))
        

        #Take all digits and multiply them together
        n = math.prod(listOfNumbers)
        print("Product of List: ", n)

        #Repeat until there is only one digit

        if len(listOfNumbers) <= 1:
            break
        else:
            iteration += 1

    return iteration

