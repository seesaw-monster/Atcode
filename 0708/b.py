N=int(input())

a=[]
b=[]
for i in range(N):
    a.append([])
    b.append('')
    s=input()
    for j in range(N):
        a[i].append(s[j])

for i in range(N):
    if i==0:
        for j in range(N-1):
            b[i]+=f'{a[i][j]}'
        b[i+1]=f'{a[i][N-1]}'
    elif i==(N-1):
        b[i-1]=f'{a[i][0]}'+b[i-1]
        for j in reversed(range(1,N)):
            b[i]=f'{a[i][j]}'+b[i]
    else:
        b[i-1]=f'{a[i][0]}'+b[i-1]
        for j in reversed(range(1,N-1)):
            b[i]=f'{a[i][j]}'+b[i]
        b[i+1]=f'{a[i][N-1]}'

for i in range(N):
    print(b[i])
