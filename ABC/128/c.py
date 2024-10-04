# import sys
# sys.setrecursionlimit(10**6)
N, M = map(int, input().split())

S = []

for _ in range(M):
    S.append(list(map(int, input().split()))[1:])

P = list(map(int, input().split()))

count = 0
for i in range(1<<N):
    all_count = 0
    for j in range(M):
        s_count = 0
        for s in S[j]:
            if (i>>s-1) & 1:
                s_count += 1

        if s_count%2 == P[j]:
            all_count+=1
        else:
            break
    if all_count == M:
        count+=1

print(count)
