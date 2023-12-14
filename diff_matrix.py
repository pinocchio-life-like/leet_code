def diffMatrix(grid):
    m, n = len(grid), len(grid[0])
    onesRow, onesCol = [0]*m, [0]*n
    zerosRow, zerosCol = [0]*m, [0]*n

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                onesRow[i] += 1
                onesCol[j] += 1
            else:
                zerosRow[i] += 1
                zerosCol[j] += 1

    diff = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            diff[i][j] = onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]

    return diff