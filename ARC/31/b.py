import sys
sys.setrecursionlimit(10**6)

A = [list(input()) for _ in range(10)]
# print(A)

if_can = False

def search(i, j, x, y, A, B, count):
    if B[i][j]:
        return
    B[i][j] = True

    if A[i][j] != 'o' and not (i==x and j==y):
        return

    d = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    for a, b in d:
        if i+a >= 0 and i+a<10 and j+b >= 0 and j+b<10:
            search(i+a, j+b, x, y, A, B, count)

    return

def fill(x, y, A):
    count = 0
    B = [[False for _ in range(10)] for _ in range(10)]
    for i in range(10):
        for j in range(10):
            if A[i][j] == 'o' and not B[i][j]:
                count+=1
                search(i, j, x, y, A, B, count)
    return count

for i in range(10):
    for j in range(10):
        if A[i][j] != 'o':
            if fill(i, j, A)==1:
                print('YES')
                exit()

print('NO')
