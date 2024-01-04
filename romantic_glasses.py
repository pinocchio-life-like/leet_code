t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    prefix_max = [0] * n
    suffix_min = [0] * n

    prefix_max[0] = a[0]
    for i in range(1, n):
        prefix_max[i] = max(prefix_max[i-1], a[i])

    suffix_min[n-1] = a[n-1]
    for i in range(n-2, -1, -1):
        suffix_min[i] = min(suffix_min[i+1], a[i])

    for i in range(n-1):
        if prefix_max[i] <= suffix_min[i+1]:
            print("YES")
            break
    else:
        print("NO")