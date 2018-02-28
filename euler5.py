# Declan Barr 13 Feb 2018
# Euler problem 5
numberFound = False

while numberFound == False:
    for x in range(11, 21): # numbers from 1 to 10 don't need to be checked as numbers 11 to 20 are multiples of these
        if i % x == 0:
            if x == 20:
                numberFound = True
                break
        else:
            break
    break
if numberFound == True:
    break
               
print(i)