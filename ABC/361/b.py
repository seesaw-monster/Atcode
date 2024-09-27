a, b, c, d, e, f = map(int, input().split())
g, h, i, j, k, l = map(int, input().split())

"""

b1 = (g<=d and g>=a) or (j<=d and j>=a)
b2 = (h<=e and h>=b) or (k<=e and k>=b)
b3 = (i<=f and i>=c) or (l<=f and l>=c)
if b1 and b2 and b3:
    print("Yes")
else:
    print("No")

"""

b1 = (g>=d or j<=a)
b2 = (h>=e or k<=b)
b3 = (i>=f or l<=c)

if b1 or b2 or b3:
    print("No")
else:
    print("Yes")
