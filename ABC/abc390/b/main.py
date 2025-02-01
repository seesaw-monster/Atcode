# import sys
# sys.setrecursionlimit(10**6)
# from collections import deque
from decimal import Decimal
N = int(input())
A = list(map(int, input().split()))

diff = Decimal(str(A[1]))/Decimal(str(A[0]))

for i in range(1, N-1):
    if Decimal(str(A[i+1]))/Decimal(str(A[i]))!=diff:
        print('No')
        exit()

print('Yes')
