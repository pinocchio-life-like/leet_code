t = int(input().strip())
for _ in range(t):
    pos = input().strip()
    col, row = pos[0], pos[1]
    moves = []
    for c in 'abcdefgh':
        if c != col:
            moves.append(c + row)
    for r in '12345678':
        if r != row:
            moves.append(col + r)
    print("\n".join(moves))