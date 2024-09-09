H, W = map(int, input().split())
si, sj = map(int, input().split())
C = [input() for _ in range(H)]
X = input()

si -= 1; sj -= 1

for i in range(len(X)):
    if X[i] == 'L':
        if sj != 0:
            if C[si][sj-1] == '.':
                sj -= 1
    if X[i] == 'R':
        if sj != W-1:
            if C[si][sj+1] == '.':
                sj += 1
    if X[i] == 'U':
        if si != 0:
            if C[si-1][sj] == '.':
                si -= 1
    if X[i] == 'D':
        if si != H-1:
            if C[si+1][sj] == '.':
                si += 1

print(si+1, sj+1)
