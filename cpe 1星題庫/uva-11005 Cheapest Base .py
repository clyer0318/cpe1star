t = int(input())
for case in range(1, t+1):
    cost = []
    for i in range(4):
        cost += list(map(int, input().split()))
    q = int(input())
    print(f"Case {case}:")

    for i in range(q):
        n = int(input())

        answer = []
        min_cost = 999999999

        for base in range(2, 37):
           
            x = n
            total = 0

            if x == 0:
                total = cost[0]

            while x > 0:
                digit = x % base
                total += cost[digit]
                x //= base

            if total < min_cost:
                min_cost = total 
                answer = [base]
            elif total == min_cost:
                answer.append(base)
        print(f"Cheapest base(s) for number {n}:", *answer)
