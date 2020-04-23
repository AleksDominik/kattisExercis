import sys 
import math
line1=sys.stdin.readline()
n_periods=int(line1.split(" ")[0])
w=int(line1.split(' ')[1])
h=int(line1.split(' ')[2])
diago=math.sqrt(w**2+h**2)
seq=[]
out=''
for i in range(n_periods):
    c=sys.stdin.readline()
    c=int(c)
    seq.append(c)
    if( c <=diago):
        out+='DA '

        
    else:
        out+='NE '
out=out[:-1]
sys.stdout.write(out)