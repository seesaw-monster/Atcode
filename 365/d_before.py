N = int(input())
S = input()

if S[0] == 'R':
    dp = {'P': 1}
elif S[0] == 'P':
    dp = {'S': 1}
else:
    dp = {'R': 1}

for i in range(1, N):
    new_dp = {}

    if S[i] == 'R':
        for key, val in dp.items():
            if key == 'P':
                if 'R' not in new_dp:
                    new_dp['R'] = val
                else:
                    new_dp['R'] = max(new_dp['R'], val)
            else:
                if 'P' not in new_dp:
                    new_dp['P'] = val + 1
                else:
                    new_dp['P'] = max(new_dp['P'], val + 1)
    elif S[i] == 'P':
        for key, val in dp.items():
            if key == 'S':
                if 'P' not in new_dp:
                    new_dp['P'] = val
                else:
                    new_dp['P'] = max(new_dp['P'], val)
            else:
                if 'S' not in new_dp:
                    new_dp['S'] = val + 1
                else:
                    new_dp['S'] = max(new_dp['S'], val + 1)
    else:
        for key, val in dp.items():
            if key == 'R':
                if 'S' not in new_dp:
                    new_dp['S'] = val
                else:
                    new_dp['S'] = max(new_dp['S'], val)
            else:
                if 'R' not in new_dp:
                    new_dp['R'] = val + 1
                else:
                    new_dp['R'] = max(new_dp['R'], val + 1)

    dp = new_dp

print(max(dp.values()))

