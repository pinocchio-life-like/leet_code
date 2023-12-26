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

dist1 = [92,41,28,84,64,51,83,59,19,34,18,32,96,72,69,34,96,75,55,75,52,47,29,18,66,64,12,97,7,15,20,81,21,88,55,77,9,50,49,77,60,68,33,71,2,88,93,15,88,69,97,35,99,83,44,15,38,56,21,59,1,93,93,34,65,98,23,65,14,81,39,82,65,78,26,20,48,98,21,70,100,68,1,77,42,63]
hour1 = 78

result1 = minSpeedOnTime(dist1, hour1)
print(result1)


dist2 = [1, 1, 100000]
hour2 = 100000

result2 = minSpeedOnTime(dist2, hour2)
print(result2)
