N, Q = map(int, input().split())
A = list(map(int, input().split()))
A = sorted(A)

B = []

for _ in range(Q):
    b, k = map(int, input().split())
    B.append((b, k))

B = sorted(B, key=lambda x: x[0])

start_i = 0

for b, k in B:
    # 最大の距離
    min_d = 0
    max_d = max(abs(A[-1] - b), abs(b - A[0]))

    while min_d < max_d:
        X = (min_d + max_d) // 2

        # 距離X 以下の範囲を探す
        left = 0
        right = N - 1

        if right-left+1 == k:
            print(max(abs(A[left] - b), abs(A[right] - b)))
            break
        elif right-left+1 < k:
            min_d = X+1
        else:
            max_d = X
