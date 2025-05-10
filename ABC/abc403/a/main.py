# import sys
# sys.setrecursionlimit(10**6)
# from collections import deque, defaultdict
N = int(input())
A = list(map(int, input().split()))

sum_m = 0

for i in range(0, N, 2):
    sum_m+=A[i]

print(sum_m)
