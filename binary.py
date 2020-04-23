import random
array=range(0,444445)
array=[k for k in array if random.randint(0,5)%2 ]

# print(array)

def binary(array,x):
    mid=int(len(array)/2)
    
    if x==array[mid]:

        return array[mid]
    elif len(array)==1:
        return -1

    elif x> array[mid]:

        return binary(array[mid:],x)
    else:
        return binary(array[:mid],x)
# print(binary(array,5))

def exponetial(array,x):
    sub=array[:1]
    ind=1
    while sub[-1]<x and ind<len(array):
        ind+=2
        sub=array[:ind]
    return binary(sub[ind/2: ind],x)
# print(exponetial(array,5))

def sublistsearch(array1,array2):
    for k in range(len(array2)):
        sub=array2[k:]
        if len(sub)<len(array1):
            return -1


        for m in range(len(array1)):
            if array1[m]!=sub[m]:
                break
            if m==len(array1)-1:
                return 'array found'
        return -1

print(sublistsearch(range(4,5), range(4,15)))
