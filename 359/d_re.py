N, K = map(int, input().split())
S = input()

dp = {'C'*K: 0}

for i in range(N):
    tmp = {}
    if S[i]!='A':
        for k, v in dp.items():
            new_k = k[1:]+'B'
            if new_k == new_k[::-1]:
                continue

            if new_k in tmp.keys():
                tmp[new_k]+=max(1, v)
            else:
                tmp[new_k]=max(1, v)

    if S[i]!='B':
        for k, v in dp.items():
            new_k = k[1:]+'A'
            if new_k == new_k[::-1]:
                continue

            if new_k in tmp.keys():
                tmp[new_k]+=max(1, v)
            else:
                tmp[new_k]=max(1, v)

    dp = tmp

print(sum(dp.values())%998244353)
