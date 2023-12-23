def minSpeedOnTime(dist, hour):
    # Binary search for the minimum speed
    left = 1
    right = 10**7 + 1

    while left < right:
        speed = (left + right) // 2
        total_time = sum(math.ceil(d / speed) for d in dist[:-1]) + dist[-1] / speed

        if total_time <= hour:
            right = speed
        else:
            left = speed + 1

    return left if left <= 10**7 else -1
