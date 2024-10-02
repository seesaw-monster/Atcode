# import sys
# sys.setrecursionlimit(10**6)
N, M, K = map(int, input().split())
A = list(map(int, input().split()))

sum_A = sum(A)
lest = K - sum_A
print(lest)
