# finalresult= "seperator".join(name)
# name shoulb be iterable it can ba list,tuple,set,dictionary but it shoud bein form of sting)
list_to_itr =['1','2','3','4']
result = " ".join(list_to_itr)

print(result)
print(id(result))  #location of result in memory
print(type(result)) #type of datatype


# dict_to_itr={"ram":"500","shyam":"600","mohan":"800"}  in dictionary it works only keys not values
dict_to_itr={"ram":500,"shyam":600,"mohan":800}
result1 = "#".join(dict_to_itr)
print(result1)


query =""" select * from tbl_class where section = 1"""
dict_new = [{"name":"shyam","age":15,"class":10},{"name":"ram","age":18,"class":12}]
newlist = []
for data in dict_new:
    inner=[]
    for key,value in data.items():
        inner.append(f'{key} = "{value}"')
        # print(inner)
    newlist.append("(" + " AND ".join(inner) + ")")
# print(newlist)
seperator =" or "
added_query = seperator.join(newlist)
# print(added_query)  
main_query = query+' and '+ added_query
print(main_query)  





