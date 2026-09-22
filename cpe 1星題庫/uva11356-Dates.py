months = [
    "January", "February", "March",
    "April", "May", "June",
    "July", "August", "September",
    "October", "November", "December"
]

days = [31, 28, 31, 30, 31, 30,
        31, 31, 30, 31, 30, 31]

case = 1

T = int(input())
for _ in range(T):
    date = input().split('-')
    year = int(date[0])
    month = months.index(date[1]) + 1
    day = int(date[2])

    i = int(input())

    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    else:
        leap = False
    
    if leap:
        date[1] = 29

    while i > 0:
        
        day += 1
        i = i - 1

        if day > days[month - 1]:
            day = 1
            month += 1

            if month > 12:
                month = 1
                year += 1
    print(f"Case {case}: {year}-{months[month - 1]}-{day:02d}")
    case += 1
    #02d:把數字補成 2 位數，不夠的前面補 0   #sep='-' : 以 - 連接
