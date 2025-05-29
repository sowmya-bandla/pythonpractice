import pandas as pd 
orders= pd.DataFrame({
    'orderID':['o101', 'o102', 'o103','o104', 'o105'],
    'customerID': ['c1', 'c2', 'c3', 'c7', 'c2'],
    'city': ['hyd', 'bng', 'viz', 'chen', 'hyd'],
    'product':['laptop', 'mobile', 'tv', 'washer', 'dryer'],
    'amount': [1000, 500, 600, 200, 400]

})
print (orders)
print('==========================')

pivot= orders.pivot_table( index= 'orderID', values='amount', columns='customerID', aggfunc= ['mean','sum'], fill_value=0)
print(pivot)