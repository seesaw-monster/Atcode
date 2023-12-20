N = int(input())
A = list(map(int,input().split()))
s=''

sum=0
for i in range(len(A)):
    sum+=A[i]
    if i%7==6:
        s+=f'{sum} '
        sum=0

print(s[:-1])
