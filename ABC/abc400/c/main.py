# import sys
# sys.setrecursionlimit(10**6)
from collections import deque, defaultdict
from decimal import Decimal

def judge(a, b, x):
    return 2**a * b**2 == x

N = int(input())

# d = deque()
d = []

s = 2

while s <= N:
   d.append(s)
   s *= 2

# print(d)

c = 0
idx = len(d)-1
for b in range(1, int(N**(1/2))+1, 2):
    while idx>=0 and d[idx]*(b**2)>N:
        idx-=1

    if idx<0:
        break

    # print(idx+1)
    c += idx+1

print(c)
