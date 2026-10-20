while True:
    
    n = int(input())
    if n == 0:
        break
    queue = list(range(1, n + 1))
    discarded = []

    while(len(queue) > 1):
        discarded.append(queue.pop(0))
        queue.append(queue.pop(0))

    if discarded:
        print(f"Discarded cards: {', '.join(map(str, discarded))}")
    else:
        print("Discarded cards:")
    print(f"Remaining card: {queue[0]}")

