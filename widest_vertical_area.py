def maxWidthOfVerticalArea(points):
    sorted_points = sorted(points, key=lambda x: x[0])
    max_width = 0
    for i in range(1, len(sorted_points)):
        width = sorted_points[i][0] - sorted_points[i-1][0]
        max_width = max(max_width, width)
    return max_width
