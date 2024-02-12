import numpy

n, m = map(int, input().split())
a= (numpy.array([input().split() for _ in range(n)], dtype=int))
#numpy.set_printoptions(legacy='1.13')
print(numpy.mean(a,1))
print(numpy.var(a,0))
#print('%.11f'%numpy.std(a,None))
print(numpy.std(a,None))