# Declan Barr 13 Feb 2018
# Euler problem 5

numberFound = False

while numberFound != True:
    # Testing to see if program able to finish when numberFound = true 
    for i in range(232790000, 232793000, 20): #i can increment in 20 as all the numbers need to be divisable by 20
        for x in range(11, 21): # numbers from 1 to 10 don't need to be checked as numbers 11 to 20 are multiples of these
            print("i is :", i, "x is :", x)
            if i % x == 0:
                numberFound = True # This does not exit the while loop as intended
            else:
                break
                
            
print(i)
