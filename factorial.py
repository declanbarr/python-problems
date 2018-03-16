# Declan Barr 16 Mar 2018
# Script that uses a function to calculate the factorial of a number

def factorial(factstart):
    for x in range(factstart, 1, -1):
        x = x * (x - 1)
    return x

print("The factorial of 7 is : ", factorial(7))