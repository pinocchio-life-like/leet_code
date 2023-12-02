def squareIsWhite(coordinates: str) -> bool:
    letter = coordinates[0]
    number = int(coordinates[1])
    
    if (ord(letter) - ord('a') + number) % 2 == 0:
        return False
    else:
        return True
