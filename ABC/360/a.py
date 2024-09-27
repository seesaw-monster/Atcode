S = input()

R = 0
M = 0

for i in range(len(S)):
    if S[i] == 'R':
        R = i
    elif S[i] == 'M':
        M = i

if R < M:
    print('Yes')
else:
    print('No')
