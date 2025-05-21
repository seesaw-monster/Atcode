N, D = map(int, input().split())
A = list(map(int, input().split()))

cnt = [0 for _ in range(10**6+1)]

for a in A:
    cnt[a]+=1

count = 0
if D==0:
    for c in cnt:
        count += max(c-1, 0)
else:
    for si in range(D):
        dp = [[0, 0]]
        for i in range(si, 10**6+1, D):
            dp.append([
                dp[-1][1],
                cnt[i]+min(dp[-1])
            ])
        count+=min(dp[-1])

print(count)
