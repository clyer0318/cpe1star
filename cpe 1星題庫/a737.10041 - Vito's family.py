#a737.10041 - Vito's family
n = int(input())
for _ in range(n):
    data = list(map(int, input().split()))

    r = data[0]
    houses = data[1:]

    houses.sort()
    mid = houses[r // 2] # 中位数

    total = 0
    for house in houses:
        total += abs(house - mid)
    print(total)
