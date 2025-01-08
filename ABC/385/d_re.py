from collections import defaultdict
N, M, sx, sy = map(int, input().split())

X = defaultdict(set)
Y = defaultdict(set)
already = set()

for _ in range(N):
    x, y = map(int, input().split())
    X[y].add(x)
    Y[x].add(y)

x, y = sx, sy
count = 0

for _ in range(M):
    d, c = input().split()
    c = int(c)

    if d=='U':
        if Y[x]!=set():
            for ny in Y[x]:
                if (y <= ny <= y+c):
                    Y[x].remove(ny)
                    count+=1
                    if Y[x]==set():
                        break
        y += c
    elif d=='D':
        if Y[x]!=set():
            for ny in Y[x]:
                if (y-c <= ny <= y):
                    Y[x].remove(ny)
                    count+=1
                    if Y[x]==set():
                        break
        y-=c
    elif d=='L':
        if X[y]!=set():
            for nx in X[y]:
                if (x-c <= nx <= x):
                    X[y].remove(nx)
                    count+=1
                    if X[y]==set():
                        break
        x-=c
    else:
        if X[y]!=set():
            for nx in X[y]:
                if (x <= nx <= x+c):
                    X[y].remove(nx)
                    count+=1
                    if X[y]==set():
                        break
        x+=c

print(x, y, count)
