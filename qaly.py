import sys
n_periods=int(sys.stdin.readline())
seq=[]
for i in range(n_periods):
    c=sys.stdin.readline()
    c=str(c)
    seq.append(c)
seq=[i.split(' ') for i in seq]
sys.stdout.write(str(sum([float(j[0])*float(j[1]) for j in seq ])))
