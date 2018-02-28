# Declan Barr 13 Feb 2018
# Euler problem 5
numberFound = False

commonMultiple = 2520 * 11 * 12 * 13 * 14 * 15 * 16 * 17 * 18 * 19 * 20 # 2520 is the lcm of 1 to 10

for i in range(2520, commonMultiple, 2520): #Lower bound can start at 2520 as this is the LCM of 1 to 10. The step can also be 2520

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