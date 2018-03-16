# Declan Barr 16 Mar 2018
# Script that uses a function to calculate the factorial of a number

def factorial(factstart):
    y = factstart
    for x in range(factstart -1, 1, -1):
        y = x * y
    return y

print("The factorial of 5 is : ", factorial(5))
print("The factorial of 7 is : ", factorial(7))
print("The factorial of 10 is : ", factorial(10))


factcheck10 = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
factcheck7 = 7 * 6 * 5 * 4 * 3 * 2 * 1
factcheck5 = 5 * 4 * 3 * 2 * 1

print("The factorial of 5 is : ", factcheck5)
print("The factorial of 7 is : ", factcheck7)
print("The factorial of 10 is : ", factcheck10)