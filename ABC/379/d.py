# import sys
# sys.setrecursionlimit(10**6)
N = int(input())
Q = []

T = 0
L = []

for _ in range(N):
    Q.append(list(map(int, input().split())))

for q in Q:
    if q[0]==1:
        L.append(-T)
    elif q[0]==2:
        T+=q[1]
    else:
        H = q[1]-T
        t = -1

        # print(L, T, H)
        for i in range(len(L)):
            if L[i] < H:
                t = i
                break

        print(len(L) if t==-1 else len(L[:t]))
        L = [] if t==-1 else L[t:]
