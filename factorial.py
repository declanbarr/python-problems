# Declan Barr 16 Mar 2018
# Script that uses a function to calculate the factorial of a number

def factorial(factstart):
    for x in range(factstart, 1, -1):
        print(x)
        x = x * (x - 1)
        print(x)
    return x
 
print("The factorial of 5 is : ", factorial(5))
print("The factorial of 7 is : ", factorial(7))
print("The factorial of 10 is : ", factorial(10))
