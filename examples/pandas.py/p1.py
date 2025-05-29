import pandas as pd
data=pd.Series([1,3,5])
print(data)
print(data.values)
print(data.index)

d1=pd.Series([1.25,4.5,6.7,3.9],index=['a','b','c','d'])
print(d1)
print(d1.values)
print(d1.index)
print('==============')
d2=pd.Series({2:'a',1:'b',3:'c'},index=[3,1])
print(d2)
print('==============')

population_dict={'cali':1234, 'texas':2345, 'ny':3456, 'florida':4567, 'illi':5678}
area_dict={'cali':987, 'texas':876, 'ny':765, 'florida':654, 'illi':543}
population=pd.Series(population_dict)
area=pd.Series(area_dict)
states=pd.DataFrame({'population':population, 'area':area})
print(states)
print(states.index)
print(states.columns)
print(pd.DataFrame(states,columns=['area']))
print('==============')

d=[{'a':10,'b':20},{'a':30,'c':40},{'d':50,'b':60}]
df=pd.DataFrame(d)
print(df)
print('==============')

import numpy as np
d3 =pd.DataFrame(np.random.randint(10,50,(4,4)),
columns=['a','b', 'c', 'd'],
index=['a1', 'a2', 'a3', 'a4'])
print(d3)
print('==============')

z=np.ones(3, dtype=[('a', 'i4'), ('b', 'f4')])
d4=pd.DataFrame(z)
print(d4)

