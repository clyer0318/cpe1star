while True:
    try:
        n = int(input())
    except EOFError:
        break

    if n == 0:
        break

    elif (n % 11 == 0):
        print(f"{n} is a multiple of 11.")

    else:
        print(f"{n} is not a multiple of 11.")