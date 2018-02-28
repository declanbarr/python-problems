# Declan Barr 13 Feb 2018
# Euler problem 5 from Project Euler (https://projecteuler.net/problem=5)
# Idea to set i to an initial value of 2520 and incrementing by 2520 found on
#  https://stackoverflow.com/questions/8024911/project-euler-5-in-python-how-can-i-optimize-my-solution


numberFound = False
i = 2520  # this is the number that will be divided by numbers from 11 to 21
          # it is the lcm of the numbers 1 to 10  (see reference above)
while numberFound == False:
    for x in range(11, 21): # numbers from 1 to 10 don't need to be checked as numbers 11 to 20 are multiples of these
                            # eg 20 = 2 * 10 therefore if a number is divisable by 20
                            # it is also divisable by 2 and 10
        if i % x == 0:
            x = x + 1
            if  x == 21:    # If number = 21 at this point it means that i % 20 == 0 was true
                numberFound = True
        else:
            i = i + 2520    # i can increment in 2520 as this is the lcm of 1 to 10 (see reference above)
            break
               
print(i)