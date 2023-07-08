# -*- coding: utf-8 -*-
"""LabAssignment3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14AmccxLZvp0-GHeGrkj7a5h16ldTRDDT
"""

import numpy as np
arr1=np.loadtxt("/content/testmarks1.csv",delimiter=",",dtype=str)
arr2=np.loadtxt("/content/testmarks2.csv",delimiter=",",dtype=str)
a1=np.delete(arr1,0,axis=0)
a2=np.delete(arr2,0,axis=0)
array1 = a1.astype(float)
array2 = a2.astype(float)
print(array1)
print(array2)
print(array1.shape)
print(array2.shape)
print(np.empty_like(array1).reshape(25,2))
print(np.add(array1,array2))
print(np.subtract(array1,array2))
print(np.multiply(array1,array2))
print(np.divide(array1,array2))
print(np.vstack((array1,array2)))
print(np.hstack((array1,array2)))
print(np.max(array1,1))
print(np.min(array1,0))
print(np.max(array2))
print(np.min(array2))
print(np.sin(array1*np.pi/180))
arra1 = array1.astype(int)
arra2 = array2.astype(int)
ar1=np.array(arra1,dtype=np.uint8)
print(ar1)
ar2=np.array(arra2,dtype=np.uint8)
print(ar2)
print(np.bitwise_and(ar1,ar2))
av=arra1.view()
print(av)
ac=arra2.copy()
print(ac)
print(np.sort(ac))
print(np.nonzero(av>50))
print(np.where(ac>100))
ankur=np.array([2])
srivaths=ankur*array1
print(srivaths)

