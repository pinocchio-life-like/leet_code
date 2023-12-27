MOD = 998244353

def count_inversions(n, k, p, q):
    nk = n * k
    inversions = 0
    for i in range(nk):
        for j in range(i + 1, nk):
            if p[i // k] * (2 ** q[i % k]) > p[j // k] * (2 ** q[j % k]):
                inversions += 1
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

