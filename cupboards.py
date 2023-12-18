n = int(input())
left_open = 0
right_open = 0
for _ in range(n):
    l, r = map(int, input().split())
    left_open += l
    right_open += r

# Minimum operations for left doors and right doors
min_ops = min(left_open, n - left_open) + min(right_open, n - right_open)
print(min_ops)