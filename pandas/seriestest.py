import pandas as pd

from collections import defaultdict

data = {"a": 1, "b": 1}

data1 = defaultdict(list)
# print(data1)

for k, v in data.items():
    data1[v].append(k)
# print(data1)
print(dict(data1))
#dictionary  
data= {"name":"shyam","age":20,"sex":"male"}
data1 = {v:k for k,v in data.items()}
print(data1)

s = pd.Series([1,2,3,4])
print(s)

s = pd.Series([1,2,3,4])
s.index = ['a','b','c','d']
print(s)


s = pd.Series([1,2,3,4],index = ['a','b','c','d'])
print(s)

data= {"name":"shyam","age":20,"sex":"male"}

s = pd.Series(data)
print(s)