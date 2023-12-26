def divide_apples(n, weights):
    count_100 = weights.count(100)
    count_200 = weights.count(200)

    # Check if the total count of 100-gram apples is even
    if count_100 % 2 != 0:
        return "NO"

    # Check if there are enough 200-gram apples to balance the weights
    if count_200 % 2 != 0 and count_100 < 2:
        return "NO"

    return "YES"

# Read input
n = int(input())
weights = list(map(int, input().split()))

# Call the function and print the result
print(divide_apples(n, weights))
