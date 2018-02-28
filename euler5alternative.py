# Declan Barr 13 Feb 2018
# Euler problem 5
commonMultiple = 1 * 2 * 3 * 4 * 5 * 6 *7 * 8 * 9 * 10 * 11 * 12 * 13 * 14 *15 * 16 * 17 * 18 * 19 * 20

for i in range(2520, commonMultiple, 2520): #i can increment in 20 as all the numbers need to be divisable by 20
    
    if i % 11 == 0 and i % 12 == 0 and i % 13 == 0 and i % 14 == 0 and i % 15 == 0 and i % 16 == 0 and i % 17 == 0 and i % 18 == 0 and i % 19 == 0 and i % 20 == 0:
        print(i)
        break