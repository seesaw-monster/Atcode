import sys
from decimal import Decimal

# 素因数分解した結果を返す関数
# a -> K を割り切れる数のset 型
# c -> それぞれが出現する回数
def pf(K):
    a=set()
    c=[0]*(K+1)
    while K%2==0:
        a.add(2)
        c[2]+=1
        K //= 2
    f=3
    while f*f<=K:
        if K%f==0:
            a.add(f)
            c[f]+=1
            K //= f
        else:
            f+=2
    if K!=1:
        a.add(K)
        c[K]+=1
    return a,c

# 各A_i の値が持つa の値をそれぞれカウント
def count(s,a,ac):
    for k in a:
        while True:
            if (s//Decimal(k)!=s/Decimal(k)):
                break
            s=s/k
            ac[k]+=1

    return ac

def main(lines):
    # 入力
    N,K=map(int,lines[0].split())
    A=list(map(int,lines[1].split()))
    # K を素因数分解
    a,c=pf(K)

    # 素因数分解により求まった各数で割り切れる回数をカウント
    ac=[0]*(K+1)
    for i in range(N):
        ac=count(Decimal(A[i]),a,ac)

    # 複数回割れる数は回数に応じてわる
    for k in a:
        ac[k]//=c[k]

    # それぞれの回数のうち最小のものがこれを満たす
    min_k=10**9
    for k in a:
        if ac[k]<min_k:
            min_k=ac[k]

    # 結果の表示
    print(min_k)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
