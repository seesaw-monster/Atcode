# import sys
# sys.setrecursionlimit(10**6)
# from collections import deque, defaultdict
H, W, N = map(int, input().split())

dH = [set() for _ in range(H)]
dW = [set() for _ in range(W)]
countH = [0 for _ in range(H)]
countW = [0 for _ in range(W)]

for i in range(N):
    x, y = map(int, input().split())
    x-=1
    y-=1

    dH[x].add(y)
    dW[y].add(x)
    countH[x]+=1
    countW[y]+=1

Q = int(input())

for _ in range(Q):
    q, z = map(int, input().split())
    if q==1:
        print(dH[z])
    else:
        print(dW[z])
