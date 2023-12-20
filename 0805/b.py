N,M=map(int,input().split())

c=[x for x in range(N+1)]
for _ in range(M):
    a,b=map(int,input().split())
    c[b]=c[a]

for i in range(1,N+1):
    a=i
    new_c=0
    while True:
        new_c=c[a]
        if new_c==a:
            break
        else:
            a=new_c

    c[i]=new_c

if min(c[1:])==max(c[1:]):
    print(min(c[1:]))
else:
    print(-1)
