def divide(dividend, divisor):
    # Handle special cases
    if divisor == 0:
        return float('inf')
    if dividend == 0:
        return 0

    # Determine the sign of the result
    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

    # Convert both dividend and divisor to positive
    dividend = abs(dividend)
    divisor = abs(divisor)

    # Initialize the quotient and the current divisor
    quotient = 0
    current_divisor = divisor

    # Perform binary search
    while dividend >= divisor:
        # Check if the current divisor can be added to the quotient
        if dividend >= current_divisor:
            dividend -= current_divisor
            quotient += 1
            current_divisor <<= 1  # Multiply the current divisor by 2
        else:
            current_divisor >>= 1  # Divide the current divisor by 2

    # Apply the sign to the quotient
    quotient *= sign

    return quotient
