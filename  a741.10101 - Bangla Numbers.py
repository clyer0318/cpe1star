def sol(n, result):
    if n >= 10000000:
        sol(n // 10000000, result)
        n %= 10000000
        result.append("kuti")
    
    if n >= 100000:
        sol(n // 100000, result)
        n %= 100000
        result.append("lakh")

    if n >= 1000:
        sol(n // 1000, result)
        n %= 1000
        result.append("hajar")
    
    if n >= 100:
        sol(n // 100, result)
        n %= 100
        result.append("shata")
    
    if n:
        result.append(n)
    return result
    
Case = 1

while True:
    try:
        n = int(input())
        if n == 0:
            print(f"{Case}. 0")
        else:
            result = []
            sol(n, result)
            print(f"{Case}. {' '.join(map(str, result))}")
        Case += 1
    except EOFError:
        break

