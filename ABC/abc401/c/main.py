# import sys
# sys.setrecursionlimit(10**6)
# from collections import deque, defaultdict
N, K = map(int, input().split())

A = [1]

if K>=N+1:
    print(1)
    exit()

for i in range(1, K):
    A.append((A[-1]+1)%10**9)

for i in range(K, N):
    A.append((A[-1]+A[-1]-(A[i-K-1] if i-K-1>=0 else 0))%10**9)

# print(A)
print((A[-1]-(A[N-K-1] if N-K-1>=0 else 0))%10**9)
