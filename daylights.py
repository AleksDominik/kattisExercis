"""
Saving daylights
https://open.kattis.com/problems/savingdaylight
June 22 2005 6:24 20:37
December 22 2005 7:24 17:30
November 2 2005 6:45 17:38
January 8 1992 7:45 18:46

"""

import sys
import functools
import itertools
import operator
from  datetime import datetime, timedelta

n=[]
for i in sys.stdin:
    n.append(i)
    
# n=sys.stdin.readlines()
# print(n)
def calculate(line):
    st =datetime.strptime(line[:-6], "%B %d %Y %H:%M ")
    end=datetime.strptime(line[:-11]+line[-6:], "%B %d %Y %H:%M ")
    # print(st,end, end-st)
    print(end.strftime(f"%B {end.day} %Y ")+f'{int((end-st).total_seconds()//(60*60))} hours {int((end-st).total_seconds()%(60*60)//60)} minutes')

[calculate(k) for k in n  if k !="\n"]
