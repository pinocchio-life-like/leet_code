n, m, a, b = map(int, input().split())

if b <= m * a:
    min_tickets = n // m
    if n % m != 0:
        min_tickets += 1
    total_cost = min_tickets * b
else:
    total_cost = n * a

print(total_cost)
