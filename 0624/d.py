N=int(input())
S=input()

SS=''
i=0
k=0
c=0
while i<N:
    if S[i]=='(':
        SS+=S[k:i]
        c=1
        j=i+1
        while c>0:
            if j==N:
                SS+=S[i:]
                break

            if S[j]==')':
                c-=1
            elif S[j]=='(':
                c+=1
            j+=1
        if c==0:
            k=j
        i=j
    else:
        i+=1

if c==0:
    print(SS+S[k:])
else:
    print(SS)
