def longestSubarray(nums):
    max_length = 0
    count = 0
    prev_count = 0
    for num in nums:
        if num == 1:
            count += 1
        else:
            max_length = max(max_length, prev_count + count)
            prev_count = count
            count = 0
    max_length = max(max_length, prev_count + count)
    return max_length - 1 if max_length == len(nums) else max_length
