# import sys
# sys.setrecursionlimit(10**6)
H, W, x, y = map(int, input().split())
x -= 1
y -= 1

S = [list(input()) for _ in range(H)]
B = [[True for _ in range(W)] for _ in range(H)]

T = list(input())

count = 0 if S[x][y]!='@' else 1
B[x][y] = False
for t in T:
    # print(t, x+1, y+1, count)
    if t=='U' and (0<=(x-1)<H) and S[x-1][y]!='#':
        count += 1 if S[x-1][y]=='@' and B[x-1][y] else 0
        x-=1
    elif t=='D' and (0<=(x+1)<H) and S[x+1][y]!='#':
        count += 1 if S[x+1][y]=='@' and B[x+1][y] else 0
        x+=1
    elif t=='L' and (0<=(y-1)<W) and S[x][y-1]!='#':
        count += 1 if S[x][y-1]=='@' and B[x][y-1] else 0
        y-=1
    elif t=='R' and (0<=(y+1)<W) and S[x][y+1]!='#':
        count += 1 if S[x][y+1]=='@' and B[x][y+1] else 0
        y+=1

    B[x][y] = False

print(x+1, y+1, count)
