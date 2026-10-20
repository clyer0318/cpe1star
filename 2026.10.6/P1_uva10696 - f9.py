while True:
    n = int(input())
    if n == 0:
        break

    if n <= 100:
        print(f"f91({n}) = 91")
    elif n >= 101:
        print(f"f91({n}) = {n - 10}")
