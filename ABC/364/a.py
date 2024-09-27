N = int(input())
S = [input() for _ in range(N)]

for i in range(2, N):
    if S[i-2]=='sweet' and S[i-1]=='sweet':
        print('No')
        exit()

print('Yes')
