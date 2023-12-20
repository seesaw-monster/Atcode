N,D=map(int,input().split())
s=[]
for n in range(N):
    s.append(input())

max_date=0
now_date=0

for d in range(D):
    free=True
    for n in range(N):
        if s[n][d]=='x':
            free=False
            if now_date>max_date:
                max_date=now_date
            now_date=0
            break

    if free:
        now_date+=1

if now_date>max_date:
    max_date=now_date

print(max_date)
