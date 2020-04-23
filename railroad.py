import sys 
import math
line1=sys.stdin.readline()
X=line1.split(' ')[0]
Y=line1.split(' ')[1]
if int(Y)%2==1:
    sys.stdout.write('impossible')
else:
    sys.stdout.write('possible')