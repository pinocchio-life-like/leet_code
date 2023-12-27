MOD = 998244353

def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, inv_left = merge_sort(arr[:mid])
    right, inv_right = merge_sort(arr[mid:])
    merged, inv_merge = merge(left, right)

    return merged, inv_left + inv_right + inv_merge

def merge(left, right):
    merged = []
    inversions = 0
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inversions += len(left) - i
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, inversions

def count_inversions(n, k, p, q):
    nk = n * k
    inversions = 0
    for i in range(nk):
        for j in range(i + 1, nk):
            if p[i // k] * (2 ** q[i % k]) > p[j // k] * (2 ** q[j % k]):
                inversions += 1

    arr = [p[i // k] * (2 ** q[i % k]) for i in range(nk)]
    sorted_arr, inversions = merge_sort(arr)

    return inversions % MOD

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Read the values for n and k
    n, k = map(int, input().split())

    # Read the array p
    p = list(map(int, input().split()))

    # Read the array q
    q = list(map(int, input().split()))

    # Calculate and print the number of inversions
    inversions = count_inversions(n, k, p, q)
    print(inversions)
