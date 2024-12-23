# import sys
# sys.setrecursionlimit(10**6)
N, M, sx, sy = map(int, input().split())
XY = [tuple(map(int, input().split())) for _ in range(N)]
DC = [list(input().split()) for _ in range(M)]

XY = set(XY)
already = set()

c = 0
x = sx
y = sy
for i in range(M):
    di = DC[i][0]
    ci = int(DC[i][1])

    if di=='U':
        # y:y+ci+1 の座標
        for ny in range(y, y+ci+1):
            if (x, ny) in XY and not (x, ny) in already:
                already.add((x, ny))
                c+=1
        y+=ci
    elif di=='D':
        for ny in range(y-ci, y+1):
            if (x, ny) in XY and not (x, ny) in already:
                already.add((x, ny))
                c+=1
        y-=ci
    elif di=='L':
        for nx in range(x-ci, x+1):
            if (nx, y) in XY and not (nx, y) in already:
                already.add((nx, y))
                c+=1
        x-=ci
    else:
        for nx in range(x, x+ci+1):
            if (nx, y) in XY and not (nx, y) in already:
                already.add((nx, y))
                c+=1
        x+=ci

print(x, y, c)
