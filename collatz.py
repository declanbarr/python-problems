# Declan Barr 07 Feb 2018
# Script that applies Collatz Conjectur to a user inputted integer

n = int(input("Please type a positive number: "))

while n > 1:
    if n % 2 == 0:
        n = n / 2
        print(n)
    else:
        n = (3*n) + 1
        print(n)
