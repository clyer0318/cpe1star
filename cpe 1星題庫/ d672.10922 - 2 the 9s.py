def get_digit_sum(j):
    total = 0

    while j > 0:
        total += j % 10
        j //= 10

    return total


while True:
    try:
        n = int(input())

        if n == 0:
            break
        total = n
        degree = 0

        if n % 9 == 0:

            if n == 9:
                degree = 1
            else:
                while total >= 10:
                    total = get_digit_sum(total)
                    degree += 1
            print(f"{n} is a multiple of 9 and has 9-degree {degree}.")

        else:
            print(f"{n} is not a multiple of 9.")
    except EOFError:
        break