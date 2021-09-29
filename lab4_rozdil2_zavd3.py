
import math
import random
import numpy as np

print (' Розділ 2 завдання 3 ')
print ('  ')
#a[n][m]
n = 4
m = 5
#b = np.matrix[n,m]

b=np.matrix([[1,4,5,2,3],[4,0,-3,1,3],[4,-7,2,-1,8],[7,-2,0,5,-9]])
print (' b = ')
print(b)
print ('     ')


i0 = 0
i1 = 0
i2 = 0
i3 = 0



j0 = 0
j1 = 0
j2 = 0
j3 = 0 
j4 = 0 

for i in range(n):
    
    for j in range(m):
        
        #for n:
        
        if i == 0:
            
            i0 += b[i,j]
            si0 = i0/m
        if i == 1:
            i1 += b[i,j]
            si1 = i1/m
        if i == 2:
            i2 += b[i,j]
            si2 = i2/m
        if i == 3:
            i3 += b[i,j]
            si3 = i3/m
            
        #for m:    
        if j == 0:
            j0 += b[i,j]
            sj0 = j0/n
        if j == 1:
            j1 += b[i,j]
            sj1 = j1/n
        if j == 2:
            j2 += b[i,j]
            sj2 = j2/n
        if j == 3:
            j3 += b[i,j]
            sj3 = j3/n
        if j == 4:
            j4 += b [i,j]
            sj4 = j4/n
            
print ('  ')
print (' середні значення по рядках')
print (si0)
print (si1)
print (si2)
print (si3)


print ('  ')
print (' середні значення по стовпчиках ')
print (sj0)
print (sj1)
print (sj2)
print (sj3)
print (sj4)



