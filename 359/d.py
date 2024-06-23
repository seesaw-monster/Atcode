N, K = map(int, input().split())
S = input()

cnt = 0
for i in range(N-K+1):
    T = S[i:i+K]
    if '?' in T:
        continue
    else:
        if T==T[::-1]:
            continue

print(cnt)
