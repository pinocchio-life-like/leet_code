n = int(input())
days = list(map(int, input().split()))

while n > 0:
    for i in range(7):
        n -= days[i]
        if n <= 0:
            print(i + 1)
            break