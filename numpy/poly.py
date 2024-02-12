import numpy 
p = [float(x) for x in input().split()]
x = float(input())
print(numpy.polyval(p, x))