# import sys
# sys.setrecursionlimit(10**6)
# from collections import deque, defaultdict
N, M, Q = map(int, input().split())

can_M = [set() for _ in range(M+1)]
can_all = set()

for _ in range(Q):
    q = input()

    if q[0]=='1':
        _, x, y = map(int, q.split())
        can_M[y].add(x)
    elif q[0]=='2':
        _, x = map(int, q.split())
        can_all.add(x)
    else:
        _, x, y = map(int, q.split())
        if x in can_all or x in can_M[y]:
            print('Yes')
        else:
            print('No')
