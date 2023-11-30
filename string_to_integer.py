def myAtoi(s: str) -> int:
    # Remove leading and trailing whitespaces
    s = s.strip()
    
    # Check if the string is empty
    if not s:
        return 0
    
    # Check if the first character is a sign (+/-)
    if s[0] in ['+', '-']:
        sign = -1 if s[0] == '-' else 1
        s = s[1:]
    else:
        sign = 1
    
    # Convert the remaining characters to integer
    result = 0
    for char in s:
        if not char.isdigit():
            break
        result = result * 10 + int(char)
    
    # Apply the sign and handle overflow
    result = sign * result
    result = max(min(result, 2**31 - 1), -2**31)
    
    return result
