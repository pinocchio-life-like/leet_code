def generateParenthesis(n):
    result = []
    backtrack(result, "", 0, 0, n)
    return result

def backtrack(result, current, open_count, close_count, max_count):
    if len(current) == max_count * 2:
        result.append(current)
        return

    if open_count < max_count:
        backtrack(result, current + "(", open_count + 1, close_count, max_count)
    if close_count < open_count:
        backtrack(result, current + ")", open_count, close_count + 1, max_count)
