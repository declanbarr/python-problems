# Declan Barr 13 Feb 2018
# Euler problem 5

i = 20

x = 1

while x <= 20:
    if i % x == 0:
        x = x + 1

    else:
        i = i + 1
        x = 1
print(i)
