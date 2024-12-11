from collections import deque
H,W,D = map(int, input().split())

S = []
for _ in range(H):
    S.append(list(input()))

F = [[False for _ in range(W)] for _ in range(H)]

q = deque()

for i in range(H):
    for j in range(W):
        if S[i][j]=='H':
            q.append((i, j, 0))

Dp = [(-1, 0), (1, 0), (0, -1), (0, 1)]

c = 0
while len(q)!=0:
    x, y, d = q.popleft()
    F[x][y] = True
    if d==D:
        continue

    for a, b in Dp:
        nx = x+a
        ny = y+b
        if nx>=0 and nx<H and ny>=0 and ny<W:
            if not F[nx][ny] and not S[nx][ny]=='#':
                q.append((nx, ny, d+1))


# for i in range(H):
#     c+=sum(F[i])
# print(c)
print(sum(sum(F, [])))
