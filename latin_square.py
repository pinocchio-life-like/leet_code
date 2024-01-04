t = int(input())

for _ in range(t):
    square = [input() for _ in range(3)]
    
    # Check rows
    for row in square:
        if row.count('A') == 2:
            missing_letter = 'B'
        elif row.count('B') == 2:
            missing_letter = 'A'
        else:
            missing_letter = 'C'
    
    # Check columns
    for col in range(3):
        column = [square[row][col] for row in range(3)]
        if column.count('A') == 2:
            missing_letter = 'B'
        elif column.count('B') == 2:
            missing_letter = 'A'
        else:
            missing_letter = 'C'
    
    print(missing_letter)
