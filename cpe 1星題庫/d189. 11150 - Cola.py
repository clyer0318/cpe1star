while True:
    try:
        n = int(input())
    except EOFError:
        break

total = 0
empty = 0

while empty >= 3:
    new_bottles = empty // 3
    total += new_bottles
    empty = empty % 3 + new_bottles

if empty == 2:
    total += 1
print(total)
