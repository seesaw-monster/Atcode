N,K=map(int,input().split())
ab=[]
for i in range(N):
    ab.append(list(map(int,input().split())))

ab=sorted(ab)
# 飲む錠剤
sum_d=0
# 日数
day=0

for i in range(N):
    sum_d+=ab[i][1]

while sum_d>K:
    sum_d-=ab[day][1]
    day+=1

if day==0:
    print(1)
else:
    print(ab[day-1][0]+1)
