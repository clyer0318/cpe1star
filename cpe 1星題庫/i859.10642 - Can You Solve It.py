#i859.10642 - Can You Solve It
n = int(input())
for i in range(1, n + 1):
    x1, y1, x2, y2 = map(int, input().split())
    a = x1 + y1
    b = x2 + y2

    s1 = a * (a + 1) // 2 + x1
    s2 = b * (b + 1) // 2 + x2
    ans = s2 - s1
    print(f"Case{i}: {ans}")
