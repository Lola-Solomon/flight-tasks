import numpy
n, m = map(int, input().split())
a= (numpy.array([input().split() for _ in range(n)], dtype=int))
s=numpy.min(a, axis=1)
print(numpy.max(s))