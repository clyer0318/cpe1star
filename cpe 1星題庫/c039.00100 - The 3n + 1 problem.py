while True:
    try:
        i, j = map(int, input().split())
    except EOFError:
        break
    
    longest = 0
    for x in range(min(i, j), max(i, j) + 1):
        n = x
        counter = 1
        while n != 1:
            if n % 2 == 1:
                n = 3 * n + 1
            else:
                n = n // 2
            counter += 1
        if counter > longest:
            longest = counter
    print(i, j, longest)
