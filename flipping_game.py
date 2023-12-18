n = int(input())
a = list(map(int, input().split()))

max_diff = -1
total_ones = 0

for i in range(n):
    if a[i] == 1:
        total_ones += 1
    curr_ones = 0
    curr_zeros = 0
    for j in range(i, n):
        if a[j] == 1:
            curr_ones += 1
        else:
            curr_zeros += 1
        max_diff = max(max_diff, curr_zeros - curr_ones)

print(total_ones + max_diff)