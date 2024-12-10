# import sys
# sys.setrecursionlimit(10**6)
H, W, D = map(int, input().split())

S = []
for _ in range(H):
    S.append(list(input()))

def cal_mn(i, j, a, b):
    return abs(i-a)+abs(j-b)

all_c = []
for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            c = set()
            for a in range(H):
                for b in range(W):
                    if S[a][b] == '.' and cal_mn(i, j, a, b)<=D:
                        c.add((a,b))
            all_c.append(c)

max_c = 0
if len(all_c)==1:
    print(len(all_c[0]))
else:
    for i in range(len(all_c)-1):
        for j in range(i+1, len(all_c)):
            if max_c < len(all_c[i] | all_c[j]):
                max_c = len(all_c[i] | all_c[j])

    print(max_c)
