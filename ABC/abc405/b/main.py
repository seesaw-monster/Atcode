# import sys
# sys.setrecursionlimit(10**6)
# from collections import deque, defaultdict
N, M = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N+1):
    ok_list = [False for _  in range(M+1)]
    for a in A[:-i] if i!=0 else A:
        ok_list[a]=True

    if len(ok_list[1:])==sum(ok_list[1:]):
        continue
    else:
        print(i)
        exit()

