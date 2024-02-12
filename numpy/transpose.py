import numpy
n,m=map(int,input().split())
arr=[]
for i in range (n):
    row=list(map(int,input().split()))
    arr.append(row)
    arr1=numpy.array(arr)


print (numpy.transpose(arr1))
print (arr1.flatten())