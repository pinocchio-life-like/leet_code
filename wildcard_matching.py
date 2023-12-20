def isMatch(s: str, p: str) -> bool:
    # Initialize pointers for string and pattern
    s_ptr = 0
    p_ptr = 0
    match_ptr = 0
    star_ptr = -1
    
    while s_ptr < len(s):
        # If characters match or pattern has '?', move both pointers
        if p_ptr < len(p) and (p[p_ptr] == '?' or p[p_ptr] == s[s_ptr]):
            s_ptr += 1
            p_ptr += 1
        # If pattern has '*', update pointers and save current positions
        elif p_ptr < len(p) and p[p_ptr] == '*':
            star_ptr = p_ptr
            match_ptr = s_ptr
            p_ptr += 1
        # If pattern has reached end or characters don't match, backtrack
        elif star_ptr != -1:
            p_ptr = star_ptr + 1
            match_ptr += 1
            s_ptr = match_ptr
        else:
            return False
    
    # Skip any remaining '*' in the pattern
    while p_ptr < len(p) and p[p_ptr] == '*':
        p_ptr += 1
    
    return p_ptr == len(p)
