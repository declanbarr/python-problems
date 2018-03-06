# Declan Barr 06 Mar 2018
# Script that reads the Iris data set in and prints the four numerical values 
# on each row
# Line 9 Adapted from https://pyformat.info/

with open("data/iris.csv") as f:
    for line in f:
        contents = line.split(',')
        print('{c[0]} {c[1]} {c[2]} {c[3]}'.format(c=contents))