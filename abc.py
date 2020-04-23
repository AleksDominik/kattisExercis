# import sys
# import copy
# numbers=sys.stdin.readline()
# orders=str(sys.stdin.readline())
# numbers=sorted([int(k) for k in numbers.split(' ')])
# numbers={"A":numbers[0],"B":numbers[1],"C":numbers[2]}
# # print([numbers[k] for k in orders if k!='\n'])
# for z in [numbers[k] for k in orders if k!='\n']:
#     print(z,end=' ')

# what does the fox say
# https://open.kattis.com/problems/whatdoesthefoxsay
####
# import sys
# import copy
# def whatfoxsay():
#     case_numbers=int(sys.stdin.readline())
#     records=[]
#     for m in range(case_numbers):
#         stop=True

#         text=sys.stdin.readline().split(' ')
#         text[-1]=text[-1][:-1]
#         lines=[]
#         while stop:
#             inp=sys.stdin.readline().split(' ')
#             # print(inp)
#             if inp[-1][-2]=='?':
#                 stop=False

#             lines.append(inp[-1][:-1])
#         # print(lines)
#         records.append([k for k in text if k not in lines])

#         # print([k for k in text if k not in lines])
#     for m in records:
#         for z in m:
#             print(z, end=' ')
#         print('\n')
# whatfoxsay()

## Watch dog
# import sys
# import copy
# import statistics
# import math

# _________________
# |   #           |
# |               |
# |       *       |
# |               |
# |            *  |
# |_______________|

## the idea is to use a greedy algorithm by going through all points starting with smallest values south-west
# and for each point test is the leash going to let the dog fall

def test(leash_coordinate, point,S):
    distance=math.sqrt((leash_coordinate[0]-point[0])**2+(leash_coordinate[1]-point[1])**2)
    if (leash_coordinate[0]+distance>S )or (leash_coordinate[0]-distance<0):
        return False
    if (leash_coordinate[1]+distance>S) or (leash_coordinate[1]-distance<0):     
        return False 
    return True  
    
def watchdog():
        
    cases_number=int(sys.stdin.readline())
    for k in range(cases_number):
        S,H=[int(k) for k in sys.stdin.readline().split(" ")]
        hashes=[]
        record=[]
        for _ in range(H):
            hashes.append([int(k) for k in sys.stdin.readline().split(" ")])

        for k in range(S+1):
            for l in range(S+1):
                if (len([1  for point in hashes if test((k,l),point,S) ])==H )and( [k,l] not in hashes):
                    record.append((k,l))    
        record=sorted(record,key=lambda x:x[0])
        if(len(record))>0:
            print(' '.join([str(k) for k in record[0]]))
            
        else: 
            print('poodle')
# watchdog()

##Video speedup
# https://open.kattis.com/problems/videospeedup


# import sys
# import copy
# import statistics
# import math
# def videospeedup():   
#     n,p,k=[int(k) for k in sys.stdin.readline().split(" ")]
#     ts=[int(k) for k in sys.stdin.readline().split(" ")]
#     ts.append(k)
#     ts.insert(0,0)
#     # print(ts)

#     real_duration=0
#     for index,timestamp in enumerate(ts):
#         # print(timestamp)
#         if index==0 :
#             pass
#         else:
#             duration=timestamp-ts[index-1]
#             # print(1+(index*p/100))
#             duration=duration*(1+((index-1)*p/100))
#             real_duration+=duration
#     print(real_duration)

## tree insertion

import sys
import copy
import statistics
import math

# stop=True
# entries=[]
# record=[]
# while stop:
#     entry=sys.stdin.readline()
#     # print(entry)
   
#     if entry=="0\n":
#         stop=False
#     if len(entry.split(' '))<=1:
#         # print('break')
#         pass
#     else:
#         # print(',dhf',entry)
#         entries.append([entry])
# # print('entries',entries)
# for entry in entries:
#     entry=entry[0].split(" ")
#     entry[-1]=entry[-1][:-1]
#     print(entry)
#     entry=[int(k) for k in entry]  
#     trees=[int(k) for k in entry ]
#     ind=1
#     for k in range(1,len(trees)-2):
#         # print(k)
#         first=trees[k+1]
#         second=trees[k+2]
#         if ((first>=trees[k]) and (second>=trees[k]) ) or (((first<trees[k]) and (second<trees[k]) )):
#             ind+=1
#         elif  ((first>=trees[k]) and (second<trees[k]) ) or (((first<trees[k]) and (second>=trees[k]) )):
#             ind=ind*2
#     record.append(ind)
#     print('kdj',record)

def catalan_for_implementation():

    n=53
    T=[0]*(n+1)
    T[0]=1
    T[1]=1
    print(T)

    for i in range(2,n+1):
        for j in range(i):
            print(i-j-1,i)
            T[i]+=T[j]*T[i-j-1]

    print(T)

def catalan_recursive(n):
    ## very very slow computation 

    if n<=1:
        return 1
    
    else:
        res=0
        for j in range(n):
            res+= catalan_recursive(j)*catalan_recursive(n-j-1)
        return res
# 116157871455782434250553845880
# print(catalan_recursive(15))

    
