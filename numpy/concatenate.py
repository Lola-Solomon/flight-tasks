import numpy
n,m,p=map(int,input().split())
arr1=[]
arr2=[]
for i in range (n):
    row1=list(map(int,input().split()))
    arr1.append(row1)
    arr11=numpy.array(arr1)
    
for i in range (m):
    row2=list(map(int,input().split()))
    arr2.append(row2)
    arr22=numpy.array(arr2)
        
print(numpy.concatenate((arr11,arr22),axis=0))        