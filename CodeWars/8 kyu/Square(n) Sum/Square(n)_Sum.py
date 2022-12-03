"""
Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.

"""

def SquareSum(n):
    sum = 0
    for i in n:
        sum += i ** 2
    return sum

print(SquareSum([1,2,2,3]))