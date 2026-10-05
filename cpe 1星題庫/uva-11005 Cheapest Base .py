t = int(input())
for case in range(1, t+1):
    cost = []
    for i in range(4):
        cost += list(map(int, input().split())) #這 4 行的數字攤平連接成一個長度為 36 的一維陣列 cost
    q = int(input())
    print(f"Case {case}:")

    for i in range(q):
        n = int(input())

        answer = [] #儲存 目前遇到成本最低的進位制
        min_cost = 999999999

        for base in range(2, 37):
           
            x = n #把 n 複製給 x，因為接下來的除法會破壞原本的數值，而我們最後印出結果時還需要原本的 n
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
