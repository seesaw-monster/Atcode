# import sys
# sys.setrecursionlimit(10**6)
# from collections import deque, defaultdict
N, K = map(int, input().split())
A = list(map(int, input().split()))

result = 1
for a in A:
    result*=a

    if len(str(result))>=K+1:
        result=1

print(result)
