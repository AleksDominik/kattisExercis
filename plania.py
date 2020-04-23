import sys
import functools
n_periods=int(sys.stdin.readline())

u0=2 #point
u_1=u0
for i in range(n_periods):
    u=(2*u_1)-1 
    u_1=u
sys.stdout.write(str(u**2))