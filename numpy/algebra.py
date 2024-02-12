import numpy
n=int(input())
arr=[]
numpy.set_printoptions(legacy='1.13')
arr1=numpy.array([input().split() for _ in range (n)],float)
print (numpy.linalg.det(arr1)) 