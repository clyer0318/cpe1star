# c014.10035 - Primary Arithmetic

while True:

    n = input().split()

    if n[0] == "0" and n[1] == "0":
        break

    k = max(len(n[0]), len(n[1]))

    count = 0
    carry = 0

    for i in range(1, k + 1):

        if i <= len(n[0]):
            a = int(n[0][-i])
        else:
            a = 0

        if i <= len(n[1]):
            b = int(n[1][-i])
        else:
            b = 0

        total = a + b + carry

        if total >= 10:
            count += 1
            carry = 1
        else:
            carry = 0

    if count == 0:
        print("No carry operation.")
    elif count == 1:
        print("1 carry operation.")
    else:
        print(f"{count} carry operations.")