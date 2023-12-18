def stones_on_table(stones):
    count = 0
    for i in range(1, len(stones)):
        if stones[i] == stones[i-1]:
            count += 1
    return count

# Take input from the user
n = int(input())
stones = input()

# Example usage:
result = stones_on_table(stones)
print(result)
