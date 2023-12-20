S=list(map(int,input().split()))
if S==sorted(S):
    out=False
    for s in S:
        if s>=100 and s<=675 and s%25==0:
            continue
        else:
            out=True
else:
    out=True

if out:
    print('No')
else:
    print('Yes')
