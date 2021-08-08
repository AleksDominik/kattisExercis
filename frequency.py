"""
kattis problem
https://open.kattis.com/problems/sort
5 2
2 1 2 1 2   = 2 2 2 1 1


9 3
1 3 3 3 2 2 2 1 1 = 1 1 1 3 3 3 2 2 2

9 77
11 33 11 77 54 11 25 25 33   =11 11 11 33 33 25 25 77 54



"""

import sys
from itertools import accumulate
import operator
length= sys.stdin.readline()
tab=sys.stdin.readline()

tab=[int(num) for num in tab.split(' ')]

tab_=[tab[k] for k in range(len(tab)) if tab.index(tab[k])==k ]

d=sorted(tab_,key=lambda x: tab.count(x), reverse=True)


d=[ tab.count(k)*[str(k)] for k in d]
d=list(accumulate(d, operator.add))[-1]
# print(d)
print(' '.join(d))
