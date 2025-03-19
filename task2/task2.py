import sys

file1 = open(sys.argv[1])
file2 = open(sys.argv[2])

x_center, y_center = map(float, file1.readline().split())
radius = float(file1.readline())**2

for line in file2:
    x,y = map(float, line.split())
    d = (x - x_center)**2 + (y - y_center)**2
    if d < radius:
        print(1)
    elif d == radius:
        print(0)
    else:
        print(2)