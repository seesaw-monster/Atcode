N, T = map(int, input().split())
S = input()
X = list(map(int, input().split()))

A = []
B = []

for i in range(N):
    if S[i] == '1':
        A.append(X[i])
    else:
        B.append(X[i])

A.sort()
B.sort()

# print(A)
# print(B)

count = 0
for a in A:
    l = 0
    r = len(B)
    while l < r:
        m = (l+r)//2
        if a < B[m]:
            r = m
        else:
            l = m + 1

    left_b = l

    l = 0
    r = len(B)-1
    right_b = -1

    while l <= r:
        m = (l+r)//2
        if a + 2*T >= B[m]:
            right_b = m
            l = m + 1
        else:
            r = m - 1

    count += right_b - left_b + 1

print(count)
