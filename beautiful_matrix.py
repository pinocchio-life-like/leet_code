# Read the matrix from input
matrix = []
for _ in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

# Find the position of the number 1
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            row_moves = abs(i - 2)
            col_moves = abs(j - 2)
            total_moves = row_moves + col_moves
            print(total_moves)
            break
