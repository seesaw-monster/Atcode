# import sys
# sys.setrecursionlimit(10**6)
# from collections import deque, defaultdict
N = int(input())
A = list(map(int, input().split()))

bubunwa = 0
s = 0
for i in range(1, N):
    bubunwa += A[-i]
    s += bubunwa*A[-i-1]

print(s)
