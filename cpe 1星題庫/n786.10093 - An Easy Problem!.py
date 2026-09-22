while True:
    try:
        n = input()
    except EOFError:
        break

    total = 0
    max_digit = 0
    value = 0

    for char in n:
        if '0' <= char <= '9':
            value = ord(char) - ord('0')
        elif 'A' <= char <= 'Z':
            value = ord(char) - ord('A') + 10
        else:
            value = ord(char) - ord('a') + 36

        total += value
        max_digit = max(max_digit, value)

    answer = -1

    for i in range(max_digit + 1, 63):
        if total % (i - 1) == 0:
            answer = i
            break

    if answer == -1:
        print("such number is impossible!")
    else:
        print(answer)