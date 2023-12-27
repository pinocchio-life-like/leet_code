# matrix = []
# for i in range(3):
#     row = []
#     for j in range(3):
#         row.append(i * j)
#     matrix.append(row)

# Using nested list comprehension
matrix = [[i , j , k ] for j in range(3) for i in range(3) for k in  range(3) if i+k+j == 2]

print(matrix)