"""
https://open.kattis.com/problems/zebrasocelots 

3
Z
O
Z
=2


4
O
Z
Z
O
=9
the idea is to compute the arrangement of zo in the distance between the start and th index of each O plus one 
"""
import sys
import itertools
def comptbell():
        
    length= sys.stdin.readline()
    zoo=[sys.stdin.readline().replace("\n","") for _ in range(int(length))]
    round=0
    zoo.reverse()
    # print(zoo)
    index_os=[k  for k in range(int(length)) if zoo[k]=='O']
    # print(index_os)

    if len(index_os)==0:
        print(0)
        return -1
    elif len(index_os)==1:
        print(pow(2,max(index_os[0], 0))
            # len(list(itertools.product('ZO',repeat=max(index_os[0], 0))))
            )
        return -1

    round=len(list(itertools.product('ZO',repeat=max(index_os[0], 0))))
    # print(round)
    for indexoc in index_os[1:] :
        # print(zoo[:indexoc], indexoc)
        # print(len(list(itertools.product('ZO',repeat=max(indexoc, 0))))+1)
        round+=pow(2,max(indexoc, 0))
        # len(list(itertools.product('ZO',repeat=)))
        # print(round)
    print(round)
    return -1

if __name__=='__main__':
    comptbell()