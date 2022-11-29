#Find narcisstic numbers: A number that when digits are raised to the #of digits equals it's self
#i.e 153 = 1^3 + 5^3 + 3 ^ 3 = 1 + 125 + 27 = 153
def narcissistic(number):
    #Take number and convert to strings
    number = str(number)
    #Find Length of number
    power = len(number)
    #Square each number by length
    totals = []
    for i in number:
        totals.append(int(i) ** power)
    #Return sum and check to see if it equals original number
    total = sum(totals)
    number = int(number)

    if total == number:
        return True
        
    else:
        return False
        

print(narcissistic(7))




    
