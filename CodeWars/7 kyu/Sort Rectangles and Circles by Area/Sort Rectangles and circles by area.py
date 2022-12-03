#Note, this code 'mutates' its output? Not really sure what that means.
#Original Kata not clear on codewars, lots of heated debate on the forums about it.
import math
seq = [(4.73, 6.73), (3.17, 0.42), 8.11, (0.76, 8.27)]
def calculateArea(x):
    if type(x) == tuple:
        area = x[0] * x[1]
    else:
        area = math.pi * x ** 2
    return area

def sort_by_area(seq):
    seq.sort(key=calculateArea)
    return seq

print(sort_by_area(seq))



"""
https://www.codewars.com/kata/5a1ebc2480171f29cf0000e5/train/python

In this kata you will be given a sequence of the dimensions of rectangles ( sequence with width and length ) 
and circles ( radius - just a number ).
Your task is to return a new sequence of dimensions, sorted ascending by area.

For example,

seq = [ (4.23, 6.43), 1.23, 3.444, (1.342, 3.212) ] # [ rectangle, circle, circle, rectangle ]
sort_by_area(seq) => [ ( 1.342, 3.212 ), 1.23, ( 4.23, 6.43 ), 3.444 ]
                        4.31            , 4.75, 27.19, 37.26

"""






    
 

        
        


