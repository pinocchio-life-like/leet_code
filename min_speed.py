def minSpeedOnTime(dist, hour):
    def canReach(speed):
        return sum((d - 1) // speed + 1 for d in dist[:-1]) + dist[-1] / speed <= hour

    left, right = 1, 10**7
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if canReach(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans