# Declan Barr 19 Mar 2018
# Script that contains function sumultiply that takes two integer arguments and 
# returns their product. Does this without the * or / operators

def sumultiply(x, y):
    sumof = 0
    for i in range(1, x+1):
        sumof = sumof + y
    return sumof

print(sumultiply(11, 13))
print(sumultiply(5, 123))


