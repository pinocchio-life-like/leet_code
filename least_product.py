from sys import stdin
def solve_least_product():
    t = int(stdin.readline())  # Read the number of test cases
    result = []
    for _ in range(t):
        n = int(stdin.readline())  # Read the length of the array
        arr = list(map(int, stdin.readline().split()))  # Read the array elements

        neg_count = 0
        neg_min = float('inf')
        neg_min_index = -1

        operations = []
        for i in range(n):
            if arr[i] < 0:
                neg_count += 1
                if abs(arr[i]) < neg_min:
                    neg_min = abs(arr[i])
                    neg_min_index = i

        if neg_count % 2 == 0:
            result.append((0, []))
        else:
            operations.append((neg_min_index, 0))
            for i in range(n):
                if i != neg_min_index:
                    operations.append((i, arr[i]))
            result.append((1, operations))
    
    return result

result = solve_least_product()

for res in result:
    print(res[0])
    for op in res[1]:
        print(op[0], op[1])