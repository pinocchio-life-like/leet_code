def max_operations(t, test_cases):
    results = []
    for i in range(t):
        n = test_cases[i][0]
        s = test_cases[i][1]
        count = 0
        for j in range(n-1):
            if s[j] == 'A' and s[j+1] == 'B':
                count += 1
                s = s[:j] + 'BA' + s[j+2:]
        results.append(count)
    return results

# Example usage
t = 3
test_cases = [(2, 'AB'), (4, 'BBBA'), (4, 'AABB')]
output = max_operations(t, test_cases)
print(output)
