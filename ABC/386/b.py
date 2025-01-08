# import sys
# sys.setrecursionlimit(10**6)
S = list(input())

c = 0

i = 0
while i<len(S):
    if S[i]!='0':
        c+=1
        i+=1
    else:
        j = i+1
        while j < len(S) and S[j]=='0' :
            j+=1

        # print(j, i, j-i-1, (j-i-1)%2)
        c+=(j-i)//2
        c+=(j-i)%2
        i = j

print(c)

