list1 =[1,2,3,4]
def square(n):
    return n*n

result = list(map(square,list1))
print(f"output is square of a given list element is {result}")