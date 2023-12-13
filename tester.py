def numSpecial(mat):
    rows = len(mat)
    cols = len(mat[0])
    row_count = [0] * rows
    col_count = [0] * cols

    # Count the number of 1s in each row and column
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 1:
                row_count[i] += 1
                col_count[j] += 1

    special_count = 0

    # Check if each 1 is the only one in its row and column
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                special_count += 1

    return special_count

# Test the function
matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print(numSpecial(matrix))
            
            
