N=int(input())
S=input()

a=False
b=False
c=False

for i in range(N):
    s=S[i]
    if s=='A':
        a=True
    elif s=='B':
        b=True
    else:
        c=True

    if a and b and c:
        print(i+1)
        break
