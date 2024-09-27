N = int(input())
G = [[] for _ in range(N)]
H = [[] for _ in range(N)]
GH = [[] for _ in range(N)]
M_G = int(input())

for i in range(M_G):
    u, v = map(int, input().split())
    G[u-1].append(v-1)

M_H = int(input())
for i in range(M_H):
    a, b = map(int, input().split())
    H[a-1].append(b-1)
    if not b-1 in G[a-1]:
        GH[a-1].append(b-1)

for i in range(len(G)):
    for j in range(len(G[i])):
        if not G[i][j] in H[i]:
            GH[i].append(G[i][j])

A = []
for i in range(N-1):
    A.append(list(map(int, input().split())))

# print(H)

yen = 0
for i in range(len(H)):
    for j in range(len(H[i])):
        yen += A[i][j]

print(yen)

