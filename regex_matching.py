def isMatch(s, p):
    # Base case: if pattern is empty, check if string is also empty
    if not p:
        return not s
    
    # Check if first characters match
    first_match = bool(s) and p[0] in {s[0], '.'}
    
    # Check if pattern has a '*' character
    if len(p) >= 2 and p[1] == '*':
        # Case 1: '*' matches zero or more preceding element
        if isMatch(s, p[2:]):
            return True
        # Case 2: '*' matches one or more preceding element
        if first_match and isMatch(s[1:], p):
            return True
        return False
    
    # If no '*', check if first characters match and continue with the rest of the string and pattern
    return first_match and isMatch(s[1:], p[1:])
