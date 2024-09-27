N, T = map(int, input().split())
S = input()
X = list(map(int, input().split()))

count = 0
for i in range(N-1):
    for j in range(i+1, N):
        if S[i] == S[j]:
            continue

        if S[i] == '1':
            moved_xi = X[i] + T + 0.1
            moved_xj = X[j] - T - 0.1
            if moved_xj < moved_xi and X[i] < X[j]:
                count += 1
        else:
            moved_xi = X[i] - T - 0.1
            moved_xj = X[j] + T + 0.1
            if moved_xi < moved_xj and X[i] > X[j]:
                count += 1

print(count)
