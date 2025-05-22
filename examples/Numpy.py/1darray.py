import numpy as np
#creating 1d array
np1=np.array([1,2,33])
print(np1)

#2d array
np2=np.array([[11,22,33],[44,55,66]])
print(np2)

print(np2.shape)
print(np2.dtype)
print(np2.ndim)
print(np2.size)
print(np2.itemsize)

np3=np.array([[1,2,3,4],[5,6,7,8]])
a=np3.reshape(2,2,2)
print(np3)
print(a)
b=np3.reshape(4,2)
print(b)


np4=np.array([11,44,33],dtype=float)
print(np4)

np5=np.zeros((4,4))
print(np5)

np6=np.ones((3,2))
print(np6)

np7=np.full((2,3),11)
print(np7)

np8=np.linspace(2,4,8)
print(np8)
c=np8.reshape(4,2)
print(c)

np9=np.random.random((2,3))
print(np9)

np10=np.random.normal(2,3,(4,4))
print(np10)

np11=np.random.randint(1,7,(5,5))
print(np11)

np12=np.eye(4,dtype=float)
print(np12)

np13=np.arange(2,8)
print(np13)

marks=([[78,67,56],[76,75,47],[84,59,60],[67,72,54]])
m=np.array(marks)
print(m)
print(m[2][1])
print(m[1])
print(m[3][1:])
print(m[0:4,2])


np14=np.random.randint(50,100,(7,7))
print(np14)
print(np14[1:5,1:5])

print("========")

np15=np.random.randint(1,50,(4,3))
print(np15)
print(np15[::-1,:])