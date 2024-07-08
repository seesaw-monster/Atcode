"""

memo:

    文字入れ替え等の実装を関数を使った方がやりやすかったかもしれない
    辞書に石のないindexをvalueを持たせて管理しており，過去にチェックした文字列についてはset形を使った．

"""
N = int(input())
S = input()
T = input()

count = 0

old = set(S)
Next_S = {S:N}

while True:
    tmp_S = {}
    for NS, idx in Next_S.items():
        for i in range(N-1):
            if i!=idx and i!=idx+1:
                new_S = ''
                for j in range(N):
                    if j==i:
                        new_S += '.'*2
                    elif j==idx:
                        new_S += NS[i:i+2]
                    else:
                        print(j)
                        new_S[j] += NS[j]

                if new_S not in old:
                    tmp_S.append(new_S)

    if len(tmp_S)==0:
        break
    else:
        count += 1
        old.update(tmp_S)
        Next_S = tmp_S

    print(Next_S)
    input()

if count>0:
    print(count)
else:
    print(-1)
