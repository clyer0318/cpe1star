#	d097. 10038 - Jolly Jumpers
while True:
    try:
        k = list(map(int, input().split()))
        n = k[0]
        jelly = True
        visited = set()
        for i in range(1, n):
            j = abs(k[i] - k [i+1])
            if j > n - 1 or j < 1 or j in visited:
                jelly = False
                break
            visited.add(j)
                
        if jelly:
            print("Jolly")
        else:
            print("Not jolly")
    except EOFError:
        break
        

               