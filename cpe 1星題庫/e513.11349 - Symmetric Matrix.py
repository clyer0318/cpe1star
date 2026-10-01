case = 0

try:
    T = int(input())
except EOFError:
    T = 0
for case in range(1, T+1):
        
        line = input().strip()

        row = int(line.split()[-1]) #處理 "N = 3"：切開後取最後一個元素即為數字
        m = []
        for _ in range(row):
            k = list(map(int, input().split()))
            m.append(k)

        is_symmetric = True
        for i in range(row):
            for j in range(row):
                if m[i][j] < 0:
                    is_symmetric = False
                    break
                if m[i][j] != m[row - 1 - i][row - 1 - j]:
                    is_symmetric = False
                    break
            if not is_symmetric:
                break
       
        if is_symmetric:
            print(f"Test #{case}: Symmetric.")
        else:
            print(f"Test #{case}: Non-symmetric.")

