import math

t = int(input())

for _ in range(t):
    n = int(input())
    squares = list(map(int, input().split()))
    
    total_squares = sum(squares)
    square_root = math.isqrt(total_squares)
    
    if square_root * square_root == total_squares:
        print("YES")
    else:
        print("NO")
