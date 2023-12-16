def max_operations(s):
    counter = 0
    result = 0
    for ch in s:
        if ch == 'A':
            counter += 1
        elif ch == 'B' and counter > 0:
            result += 1
            counter -= 1
    return result

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    s = input().strip()
    print(max_operations(s))