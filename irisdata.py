with open("data/iris.csv") as f:
    for line in f:
        contents = line.split(',')
        print('{c[0]} {c[1]} {c[2]} {c[3]}'.format(c=contents))