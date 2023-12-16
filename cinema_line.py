def can_sell_tickets(n, bills):
    change_25 = 0
    change_50 = 0

    for bill in bills:
        if bill == 25:
            change_25 += 1
        elif bill == 50:
            if change_25 >= 1:
                change_25 -= 1
                change_50 += 1
            else:
                return "NO"
        elif bill == 100:
            if change_50 >= 1 and change_25 >= 1:
                change_50 -= 1
                change_25 -= 1
            elif change_25 >= 3:
                change_25 -= 3
            else:
                return "NO"

    return "YES"

n = int(input())
bills = list(map(int, input().split()))

result = can_sell_tickets(n, bills)
print(result)
