n = int(input())  # number of friends
fingers = list(map(int, input().split()))  # fingers shown by each friend

count = 0
for i in range(1, 6):
    total_fingers = sum(fingers) + i
    if total_fingers % (n + 1) != 1:
        count += 1

print(count)
