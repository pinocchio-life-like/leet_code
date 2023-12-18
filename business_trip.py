k = int(input())
growth = list(map(int, input().split()))

# Sort the growth rates in descending order
growth.sort(reverse=True)

# Add up the growth rates until the total growth is at least k
total_growth = 0
months = 0
for g in growth:
    if total_growth >= k:
        break
    total_growth += g
    months += 1

# Check if the total growth is less than k
if total_growth < k:
    print(-1)
else:
    print(months)