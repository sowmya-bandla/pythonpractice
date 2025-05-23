import numpy as np
a=np.random.randint(50,100,(3,4))
print(a)
print('===============')
#rowwise reverse
b=a[::-1,:]
print(b)
print('===============')
#columnwise reverse
c=a[:,::-1]
print(c)
print('===============')
#bothwise reverse
d=a[::-1,::-1]
print(d)
print('===============')


#concatination
a1=np.random.randint(1,10,(4,4))
print(a1)
print('===============')
a2=np.ones((4,4), dtype=int)
print(a2)
print('===============')
#row wise
a3=np.concatenate((a1,a2),axis=1)
print (a3)
print('===============')
#column wise
a4=np.concatenate((a1,a2),axis=0)
print(a4)
print('===============')



 
