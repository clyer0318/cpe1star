while True:
    try:
        n = int(input())
    except EOFError:
        break

    total = n
    empty = n

    while empty >= 3:
        new_bottles = empty // 3
        total += new_bottles
        empty = new_bottles + (empty % 3)

    if empty == 2:
        total += 1
    print(total)