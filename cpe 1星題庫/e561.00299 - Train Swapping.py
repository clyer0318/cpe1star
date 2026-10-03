#e561.00299 - Train Swapping
N = int(input())
for _ in range(N):
    L = int(input())
    m = list(map(int, input().split()))
    total = 0
    for _ in range(L - 1):
        for i in range(L - 1):
            if m[i] > m[i + 1]:
                m[i], m[i + 1] = m[i + 1], m[i]
                total += 1
    print(f"Optimal train swapping takes {total} swaps.")