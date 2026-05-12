set1 = {1,2,3,4,4,6,2,56}
# print(type(set1))

for i in set1:
    pass
set2 =set()
# print(type(set2))
for i in range(1,11,1):
    set2.add(i)
set2.add(5)


print(set2)
print(set1)
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.isdisjoint(set2))
print(set1.issuperset(set2))





list1      = set([1,2,3,4,5,6])
list2      = set([4,5,6,7,8])
missvalue  = list1-list2
missvalue2 = list2-list1
print(missvalue)
print(missvalue2)





