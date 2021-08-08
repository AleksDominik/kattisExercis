"""
kattis problem 

https://open.kattis.com/problems/queens

8
1 5
6 2
3 1
5 0
4 6
0 3
2 7
7 4
 = CORRECT
4
2 3
1 0
0 2
3 1
CORRECT

4
2 3
0 2
1 0
2 2
INCORRECT

3                                                                                                
2 0
1 1
0 2


"""

import sys

N= int(sys.stdin.readline())
lines=[sys.stdin.readline() for k in range(int(N))]
lines=[k.replace("\n",'').split() for k in lines]
tab=[N*[0] for _ in range(N)]
for queen in lines:
    tab[int(queen[0])][int(queen[1])]=1


# for k in tab:
#     # print(k)
def sumcol(tab, col):
    return sum(tab[col])
def sumline(tab, line):
    return sum([tab[i][line] for i in range(N)])
def sumdiagonal1(tab, diago):
    # print('diago', diago)
    sum=0
    k=0
    while diago[0]+k<N and diago[1]+k<N:
        sum+=tab[diago[0]+k][diago[1]+k]
        k+=1
    # print('the sum is ',sum)
    return sum
def sumdiagonal2(tab, diago):
    # print('diago', diago)

    sum=0
    k=0
    while diago[0]+k<N and diago[1]-k>=0:
        sum+=tab[diago[0]+k][diago[1]-k]
        k+=1
        # print(diago[0]-k, diago[1]-k)
    return sum



sumcolumns=max([sumcol(tab,k) for k in range(N)])
sumlines=max([sumline(tab,k) for k in range(N)])
# print([ sumdiagonal1(tab,[0,n]) for n in range(n)  ]+ [ sumdiagonal1(tab,[n,0]) for n in range(n)  ] )
# print([ sumdiagonal2(tab,[n,N-1]) for n in range(N)  ]+ [ sumdiagonal2(tab,[0,n]) for n in range(N)  ] )
sumdiago1=max([ sumdiagonal1(tab,[0,n]) for n in range(N)  ]+ [ sumdiagonal1(tab,[n,0]) for n in range(N)  ] )
sumdiago2=max([ sumdiagonal2(tab,[n,N-1]) for n in range(N)  ]+ [ sumdiagonal2(tab,[0,n]) for n in range(N)  ] )

# print(sumcolumns, sumlines, sumdiago1, sumdiago2)

if sumcolumns>1 or sumlines>1 or sumdiago1>1 or sumdiago2>1:
    print('INCORRECT')
else:
    print('CORRECT')