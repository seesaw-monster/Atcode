n = int(input())
x = int(input())
A = list(map(int, input().split()))

min_len = float('inf')

s = A[0]
r = 1
for l in range(n):
    if r != n:
        while s<=x:
            s += A[r]
            r += 1
            if r == n:
                break

    # print(l, r, s)
    if r-l<min_len and s > x:
        min_len = r-l

    s -= A[l]

print(min_len)
