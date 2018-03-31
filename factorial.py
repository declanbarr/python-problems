# Declan Barr 16 Mar 2018
# Script that uses a function to calculate the factorial of a number

def factorial(factstart):
    factAns = factstart # factAns is assigned the number for which you wish to find the factorial
    for x in range(factstart -1, 1, -1): # The for loop provides all the number below the number 
                                         # you wish to find the factorial of
                                         # For loop increments down rather than up
        factAns = factAns * x        
    return factAns
 
print("The factorial of 5 is : ", factorial(5))
print("The factorial of 7 is : ", factorial(7))
print("The factorial of 10 is : ", factorial(10))
