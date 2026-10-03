#e579.10050 - Hartals

T = int(input())
for _ in range(T):
    N = int(input())
    P = int(input())

    h = []
    total = 0
    for _ in range(P):
        h.append(int(input()))

    for i in range(1, N + 1):
        if i % 7 == 6 or i % 7 == 0:
            continue

        for j in range(P):
            if i % h[j] == 0:
                total += 1
                break
    print(total)
