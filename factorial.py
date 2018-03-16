# Declan Barr 16 Mar 2018
# Script that uses a function to calculate the factorial of a number

def factorial(factstart):
    y = factstart
    for x in range(factstart -1, 1, -1):
        print(x, y)
        y = x * y
        print(x, y)
    return y

print("The factorial of 5 is : ", factorial(5))