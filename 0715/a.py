N,P,Q=map(int,input().split())

d=list(map(int,input().split()))

min_d=d[0]
for i in range(1,N):
    if min_d>d[i]:
        min_d=d[i]

if P<=Q+min_d:
    print(P)
else:
    print(Q+min_d)
