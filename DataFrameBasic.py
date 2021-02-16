import pandas as pd
import numpy as np
# d1 = pd.DataFrame(np.random.randn(3,4),columns = ['a','b','c','d'])
# print("d1 is:\n", d1)
# d2 = pd.DataFrame(np.random.randn(2,3),columns = ['a','e','c'])
# d = pd.concat([d1, d2], ignore_index=True)
# print(d)
# d = pd.concat([d1, d2], join = 'inner')
# print(d )
# d = pd.concat([d1, d2], join = 'outer')
# print(d )
# data = pd.DataFrame({'key1': ['one']*3 + ['two']*4, 'key2':[1,1,2,3,4,3,3]})
# print(data)
# ## check if row is same row
# duplicate = data.duplicated()
# print(duplicate)
# print(data.drop_duplicates())
# ## delete the same element with column name
# print(data.drop_duplicates(['key1']))
# print(data.drop_duplicates(['key1'], keep = 'last'))
# print(data['key1'].map(str.upper))
# data.replace(['one', 'two'], [0,1])
# print(data.replace(['one'], np.nan))
# print("original data is :\n", data)
# a = data.rename(index = {0: 'a', 1: 'b', 2: 'c', 3: 'd'})
# print(data)
# a['key2'][np.abs(a['key2']) > 2] = -np.sign(a['key2'])*8
# print(a)

## matplotlib.pyplot
import matplotlib.pyplot as plt

fig = plt.figure()
plt.scatter(np.arange(30),np.arange(30)+30 * np.random.randn(30))
f, a = plt.subplots(1)
a.scatter(np.arange(30),np.arange(30)+3 * np.random.randn(30))
a.set_xticks([0,10,20,30])
a.set_xticklabels(['a','b','c','d'])
a.set_xlabel("X")
plt.show()
plt.savefig("plt.png", dpi = 400)
