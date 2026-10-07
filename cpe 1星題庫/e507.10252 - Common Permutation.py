#e507.10252 - Common Permutation
while True:
    try:
        a = input()
        b = input()
        result = []
        used = []

        
        for i in range(len(a)):
            for j in range(len(b)):
                if a[i] == b[j] and j not in used:
                    result.append(a[i])
                    used.append(j)
                    break

        result.sort() #排序
        print("".join(result))
    except EOFError:
        break