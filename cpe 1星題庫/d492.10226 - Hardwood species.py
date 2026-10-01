n = int(input())
input()
for case in range (n):
    tree = {}
    while True:
        try:
            name = input()
            if name == "":
                break
    
            if name in tree:
                tree[name] += 1
            else:
                tree[name] = 1

        except EOFError:
            break

    total = sum(tree.values())

    for name in sorted(tree):
        percentage = tree[name] / total * 100
        print(f"{name} {percentage:.4f}") #小數點後4位

    if case != n-1:
        print()