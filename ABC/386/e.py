# import sys
# sys.setrecursionlimit(10**6)
from collections import defaultdict
N, K = map(int, input().split())
A = list(map(int, input().split()))

d = defaultdict(int)
for a in A:
    a = format(a, '060b')
    print(a)
    b = list(str(a))
    for i in range(60):
        d[i]+=1 if b[i] == '1' else 0

s = 0
c = 0
for i in range(60):
    if c>K:
        break

    if (d[i]!=N or K%2==1) and d[i]>0:
        c+=1
        s+=2**(59-i)

print(s)
