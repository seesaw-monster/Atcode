N = int(input())
X = list(map(int, input().split()))
P = list(map(int, input().split()))
sumP = [0]
for i in range(N):
    sumP.append(sumP[-1]+P[i])

Q = int(input())
for i in range(Q):
    L, R = map(int, input().split())
    idxL = 0; idxR = 0

    l = 0;r = N
    while l < r:
        mid = (l+r)//2

        if X[mid]>=L:
            r = mid
        else:
            l = mid + 1

    idxL = l

    l = 0;r = N
    while l < r:
        mid = (l+r)//2

        if X[mid]<=R:
            l = mid + 1
        else:
            r = mid

    idxR = r
    print(sumP[idxR]-sumP[idxL])
