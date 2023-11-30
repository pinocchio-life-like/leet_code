def minimumOneBitOperations(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n ^ minimumOneBitOperations(n >> 1) << 1
