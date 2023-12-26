# Read the input sum
sum_input = input().strip()

# Split the sum by '+'
summands = sum_input.split('+')

# Sort the summands in non-decreasing order
sorted_summands = sorted(summands)

# Join the sorted summands with '+'
new_sum = '+'.join(sorted_summands)

# Print the new sum
print(new_sum)
