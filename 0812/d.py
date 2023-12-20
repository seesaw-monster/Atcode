N=int(input())
S=list(input())
Q=int(input())

low=False
is_low=False
no_count_S=[]

for _ in range(Q):
    t,x,c=input().split()

    if t=='1':
        S[int(x)-1]=c
        no_count_S.append(int(x)-1)
    elif t=='2' and not low:
        if not is_low:
            is_low=True
        low=True
    elif t=='3' and low:
        if not is_low:
            is_low=True
        low=False

    if t!='1':
        no_count_S=[]

return_s=''.join(S)
if is_low and low:
    return_s=return_s.lower()
elif is_low and not low:
    return_s=return_s.upper()

for ncS in no_count_S:
    return_s=return_s[:ncS]+S[ncS]+return_s[ncS+1:]


print(return_s)
