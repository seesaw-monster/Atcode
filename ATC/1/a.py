H, W = map(int, input().split())

C = []
D = [[] for _ in range(H)]
a = 0; b = 0

for i in range(H):
    s = input()
    if 's' in s:
        for w in range(W):
            if s[w]=='s':
                a = i
                b = w

    C.append(list(map(str, s)))
    D[i] = [False for _ in range(W)]

d = [(0, -1), (-1, 0), (0, 1), (1, 0)]

def search(i, j):
    if C[i][j] == 'g':
        return True

    D[i][j] = True

    if C[i][j] == '#':
        return False

    b = False
    for x, y in d:
        if i+x >= 0 and i+x < H and j+y >= 0 and j+y < W:
            if not D[i+x][j+y]:
                if search(i+x, j+y):
                    b = True 

    return b

if search(a, b):
    # print(D)
    # for i in range(H):
    #     s = ''
    #     for j in range(W):
    #         s += str(D[i][j])[0]
    #     print(s)
    print('Yes')
else:
    print('No')
