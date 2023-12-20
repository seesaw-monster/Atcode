n1,n2,m=map(int,input().split())

link=[]
dist=[]
for i in range(n1+n2):
    link.append([])
    dist.append(0)
    for j in range(n1+n2):
        link[i].append(0)

for _ in range(m):
    a,b=map(int,input().split())
    link[a-1][b-1]=1

max_dist=0
for i in range(n1):
    for j in range(n1+n2):
        dist[j]=0

    for j in range(n1,n1+n2):
        link[i][j]=1

        link[i][j]=0
