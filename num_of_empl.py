def numEmployees(hours, target):
    count = 0
    for h in hours:
        if h >= target:
            count += 1
    return count

