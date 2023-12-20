N,M=map(int,input().split())
P,C,F=[],[],[]
for _ in range(N):
    l = list(map(int,input().split()))
    P.append(l[0])
    C.append(l[1])
    F.append(set(l[2:]))

ans = False
for i in range(N):
    for j in range(N):
        ans |= P[i]>=P[j] and F[i]<=F[j] and (P[i]>P[j] or F[i]<F[j])

print('Yes' if ans else 'No')
