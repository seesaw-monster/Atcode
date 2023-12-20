N=int(input())
S=[]
for _ in range(N):
    S.append(str(input()))

is_yes=False
for i in range(N):
    if is_yes:
        break
    for j in range(N):
        if i==j:
            continue
        s=S[i]+S[j]
        if s==s[::-1]:
            print('Yes')
            is_yes=True
            break

if not is_yes:
    print('No')
