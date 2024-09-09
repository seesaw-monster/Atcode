N = int(input())
S = input()

def get_win(s):
    if s == 'R':
        return 'P'
    elif s == 'P':
        return 'S'
    else:
        return 'R'

def get_lose(s):
    if s == 'R':
        return 'S'
    elif s == 'P':
        return 'R'
    else:
        return 'P'

dp = {'.'+get_win(S[0]): 1, '.'+S[0]: 0}

for i in range(1, N):
    new_dp = {}

    for key, val in dp.items():
        if key[-1] == get_win(S[i]):
            if key[1:]+S[i] not in new_dp:
                new_dp[key[1:]+S[i]] = val
            else:
                new_dp[key[1:]+S[i]] = max(new_dp[key[1:]+S[i]], val)
        else:
            if key[1:]+get_win(S[i]) not in new_dp:
                new_dp[key[1:]+get_win(S[i])] = val + 1
            else:
                new_dp[key[1:]+get_win(S[i])] = max(new_dp[key[1:]+get_win(S[i])], val + 1)

            if key[1:]+S[i] not in new_dp:
                new_dp[key[1:]+S[i]] = val
            else:
                new_dp[key[1:]+S[i]] = max(new_dp[key[1:]+S[i]], val)

    dp = new_dp

print(max(dp.values()))
