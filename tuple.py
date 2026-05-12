test_tuple = (3,2,56,"true",True,2)
print(test_tuple)
# test_tuple[0]=5   
# print(test_tuple)
new_tu = ("manish",)
print(type(new_tu))
print(test_tuple[2:4])
if 3 in test_tuple:
    print("element is in present in tuple")

# print(test_tuple.count(3))
# print(len(test_tuple))
# print(test_tuple.index(3))
test_tuple1=([5,6],[6,7,8,9],[3])
# print(len(test_tuple1))
new_tuple = ()
for i in test_tuple1:
    new_var = tuple(i)
    new_tuple = new_tuple + new_var
print(new_tuple)


tuple1 = (10,2,3,5)
tuple2 = (3,6,4,3)
final_tuple=()
for i in range(len(tuple1)):
    result = tuple1[i] ** tuple2[i]
    final_tuple = final_tuple+(result,)

print(final_tuple)

