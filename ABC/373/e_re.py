N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = sorted(A)

L = K - sum(A)
C = []
for a in A:
    if not a+L >= B[-M]:
        C.append(-1)
        continue

    l = a
    r = a+L+1

    while l < r:
        mid = (l+r)//2
        if M*(mid+1) > sum(B[-M:])+(L-(mid-a)):
            r = mid
        else:
            l = mid+1

    C.append(l-a)

print(*C)
