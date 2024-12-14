# import sys
# sys.setrecursionlimit(10**6)
H, W, X = map(int, input().split())
P, Q = map(int, input().split())
P-=1
Q-=1

S = []

for _ in range(H):
    S.append(list(map(int, input().split())))

F = [[True for _ in range(W)] for _ in range(H)]

l = []

D = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for a, b in D:
    np = P+a
    nq = Q+b
    if (0<=np<H) and (0<=nq<W):
        F[np][nq] = False
        l.append([S[np][nq], np, nq])

takahashi = S[P][Q]
F[P][Q] = False

while True:
    nl = []
    l.sort()
    grouth = False
    for i in range(len(l)):
        power, x, y = l[i]
        if X*power < takahashi:
            grouth = True
            takahashi+=power
            for a, b in D:
                nx = x+a
                ny = y+b
                if (0<=nx<H) and (0<=ny<W) and F[nx][ny]:
                    F[nx][ny] = False
                    nl.append([S[nx][ny], nx, ny])
        else:
            nl.extend(l[i:])
            break

    if not grouth:
        break

    l = nl

print(takahashi)
