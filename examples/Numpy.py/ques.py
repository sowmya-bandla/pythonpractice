import numpy as np
n1=np.arange(10,50)
print(n1)

n=np.eye(3,3, dtype=int)
print(n)


n2=np.zeros(20, dtype=int)
print(n2)
n2[4::5]=1
print(n2)

n3=np.random.randint(100,200,size=15)
print(n3)

n4=np.full((4,4),7)
print(n4)

n5=np.arange(1,13)
print(n5)
reshape=np.reshape(n5,(3,4))
print(reshape)

n6=np.random.randint(10,20,(3,4))
print(n6)
print(n6[::-1,:])

n7=np.random.randint(10,50,(4,4))
print(n7)
diagonal=np.diagonal(n7)
print(diagonal)