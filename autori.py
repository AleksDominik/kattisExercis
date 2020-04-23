import sys
import functools
name=sys.stdin.readline()
c=[str(f) for f in name if f==f.upper() and f!=' ' and f !='\n' and f!='-']

sys.stdout.write(functools.reduce(lambda x,y: x+y,c ))


