# Declan Barr 13 Feb 2018
# Euler problem 5
numberFound = false

for i in range(232790000, 232793000, 20): #i can increment in 20 as all the numbers need to be divisable by 20

    while numberFound == false:
    for x in range(11, 21): # numbers from 1 to 10 don't need to be checked as numbers 11 to 20 are multiples of these
        print("i is :", i, "x is :", x)
        if i % x == 0:
            print i
            numberFound = True
            break
        else:
            break
    break            
            
print(i)