n, m, a, b = map(int, input().split())

# Calculate the minimum cost using the following logic:
# If the cost of the m ride ticket is less than or equal to m times the cost of a one ride ticket,
# it is more cost-effective to buy the m ride ticket instead of individual one ride tickets.
if b <= m * a:
    # Calculate the minimum number of m ride tickets needed to cover all rides
    min_tickets = n // m
    # If there are remaining rides that cannot be covered by the m ride tickets,
    # add the cost of a one ride ticket for each remaining ride
    if n % m != 0:
        min_tickets += 1
    # Calculate the total cost
    total_cost = min_tickets * b
else:
    # If the cost of the m ride ticket is more expensive than m times the cost of a one ride ticket,
    # it is more cost-effective to buy individual one ride tickets for each ride.
    total_cost = min(n * a, (n // m) * b + (n % m) * a)

print(total_cost)

