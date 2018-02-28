# Declan Barr 13 Feb 2018
# Euler problem 5
numberFound = False
i = 2520

while numberFound == False:
    for x in range(11, 21): # numbers from 1 to 10 don't need to be checked as numbers 11 to 20 are multiples of these
        if i % x == 0:
            x = x + 1
            if  x == 21:
                numberFound = True
        else:
            i = i + 2520
            break
    x = x + 1
               
print(i)