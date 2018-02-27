# Declan Barr 13 Feb 2018
# Euler problem 5

i = 20

for x in range(1, 21):
    if i % x == 0:
        print(i, "divided by ", x, "has remainder 0")

    else:
        i = i + 1

print(i)
