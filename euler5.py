# Declan Barr 13 Feb 2018
# Euler problem 5 from Project Euler (https://projecteuler.net/problem=5)
# Idea to set i to an initial value of 2520 and incrementing by 2520 found on
#  https://stackoverflow.com/questions/8024911/project-euler-5-in-python-how-can-i-optimize-my-solution
import math
twentyFact = math.factorial(20)  # This will be used as the upper bound for the "For i" loop

numberFound = False # numberFound will be set to true when the lcm of the number 1 to 20 has been found

for i in range(2520, twentyFact, 2520):
    for x in range(11, 21): # numbers from 1 to 10 don't need to be checked as numbers 11 to 20 are multiples of these
                            # eg 20 = 2 * 10 therefore if a number is divisable by 20
                            # it is also divisable by 2 and 10
 
        if i % x == 0:  # This checks if i is evenly divisible by x     
            if x == 20:   
                numberFound = True
        else:
            break # This breaks out of the "for x loop
    if numberFound == True: 
        break # This breaks out of the "for i" loop
               
print(i)
