# Declan Barr 13 Feb 2018
# Euler problem 5

i = 20


numberFound = False

while numberFound != True:
    for x in range(1, 21):
        if i % x == 0:
            print(i)
            numberFound = True
        else:
            i = i + 1
            x = 1
        
print(i)
