import numpy
n, m = map(int, input().split())
a= (numpy.array([input().split() for _ in range(n)], dtype=int))
s=numpy.sum(a, axis=0)
print(numpy.prod(s))