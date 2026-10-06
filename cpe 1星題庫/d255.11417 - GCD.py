def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

while True:
    n = int(input())
    if n == 0:
        break

    G = 0
    for i in range(1, n):  #這題要算的是ex:10的所有組合的gcd，包含(1,2),(1,3),(1,4)...(1,10),(2,3),(2,4)...(2,10),(3,4)...(3,10)....(9,10)
        for j in range(i + 1, n + 1):
            G += gcd(i, j)
    print(G)

