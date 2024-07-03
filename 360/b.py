S, T = map(str, input().split())

for c in range(1, len(S)):
    for w in range(c, len(S)):
        s_list = [S[i:i+w] for i in range(0, len(S), w)]

        t = ''
        for s in s_list:
            if len(s)>=c:
                t += s[c-1]

        if t == T:
            print('Yes')
            exit()

print('No')
