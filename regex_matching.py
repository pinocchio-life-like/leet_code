def isMatch(s: str, p: str) -> bool:
    # Base case: if pattern is empty, check if string is also empty
    if not p:
        return not s
    
    # Check if the first characters match
    first_match = bool(s) and p[0] in {s[0], '.'}
    
    # Check if the pattern has a '*' after the second character
    if len(p) >= 2 and p[1] == '*':
        # Case 1: '*' matches 0 occurrences of the preceding character
        # Skip the '*' and the preceding character in the pattern
        case1 = isMatch(s, p[2:])
        
        # Case 2: '*' matches 1 or more occurrences of the preceding character
        # Check if the first character matches and recursively check the remaining string and pattern
        case2 = first_match and isMatch(s[1:], p)
        
        # Return True if either case1 or case2 is True
        return case1 or case2
    
    # If the first characters match, recursively check the remaining string and pattern
    return first_match and isMatch(s[1:], p[1:])


print(isMatch('aa', 'a*'))