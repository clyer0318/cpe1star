#d306.10193 - All You Need Is Love
import math
n = int(input())
for i in range(1, n + 1):
    s1 = input()
    s2 = input()

    a = int(s1, 2) #將二進位字串 s1 轉換成十進位整數 #int(字串, 進位制)
    b = int(s2, 2)

    if math.gcd(a, b) > 1:
        print(f"Pair #{i}: All you need is love!")
    else:
        print(f"Pair #{i}: Love is not all you need!")
