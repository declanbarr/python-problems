# Declan Barr 13 Feb 2018
# Euler problem 5

i = 20


numberFound = False

while numberFound != True:
    for i in range(1, 1000000000000, 20): #i can increment in 20 as all the numbers need to be divisable by 20
        for x in range(1, 21):
            print("i is :", i, "x is :", x)
            if i % x == 0:
                numberFound = True
                
            
print(i)
