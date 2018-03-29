# Declan Barr 16 Mar 2018
# Script that uses a function to calculate the factorial of a number

def factorial(factstart):
    factAns = factstart
    for x in range(factstart -1, 1, -1):
    # For loop increments down
        factAns = x * factAns
    return factAns

print("The factorial of 5 is : ", factorial(5))
print("The factorial of 7 is : ", factorial(7))
print("The factorial of 10 is : ", factorial(10))
