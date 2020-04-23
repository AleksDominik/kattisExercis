import sys
import functools
n_periods=int(sys.stdin.readline())
seq=[]
for i in range(n_periods):

    seq.append(str(sys.stdin.readline()))

seq=[(i[:-2],i[-2]) for i in seq ]
seq=[int(i)**int(j) for i,j in seq ]
# print(seq)
sys.stdout.write(str(functools.reduce(  lambda a,b: a+ b  , seq )))
