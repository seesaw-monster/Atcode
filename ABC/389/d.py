# import sys
# sys.setrecursionlimit(10**6)
R = int(input())

"""
中心:1つ確定
X軸上：x4
x>1 and y>1 : x4

(i, j) に関して(i+0.5, j+0.5) だけ調べればいい
"""

count = 1

for i in range(1, R):
    x = i+0.5
    y = (R**2-x**2)**(1/2)
    # print(x, y)
    count += 4 if y > 0.5 else 0
    count += int(y-0.5)*4

print(count)
