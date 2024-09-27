def judge(B):
    if len(B)<=2:
        return True

    B.sort()
    diff = B[1]-B[0]
    for i in range(1, len(B)-1):
        if B[i+1]-B[i] != diff:
            return False

    return True

N = int(input())
A = list(map(int, input().split()))

dp = {}
count = []
for i in range(N):
    if str(A[i]) not in dp.keys():
        dp[str(A[i])] = 1
    else:
        dp[str(A[i])] += 1

count.append(sum(dp.values()))

for k in range(1, N+1):
    new_dp = {}
    for i in range(N):
        for key, value in dp.items():
            l = list(map(int, key.split()))
            l.append(A[i])
            if judge(l):
                sl = ' '.join(map(str, l))
                if sl not in new_dp.keys():
                    new_dp[sl] = value
                else:
                    new_dp[sl] += value

    dp = new_dp
    count.append(sum(dp.values()))

print(*count)
