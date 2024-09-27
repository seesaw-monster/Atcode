H, W = map(int, input().split())

C = ['.'*(W+2)]

for _ in range(H):
    C.append('.'+input()+'.')

C.append('.'*(W+2))

N = min(H, W)

S = [0 for _ in range(N+1)]

def check(C, i, j, N):
    if C[i][j]=='#':
        d = 1
        while d <= N:
            if C[i+d][j+d] == '#' and C[i+d][j-d] == '#' and C[i-d][j+d] == '#' and C[i-d][j-d] == '#':
                d+=1
            else:
                break

        return d-1

    return 0

for i in range(1, H+1):
    for j in range(1, W+1):
        S[check(C, i, j, N)]+=1

print(*S[1:])
