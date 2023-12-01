def minSubArrayLen(s, nums):
    n = len(nums)
    min_len = float('inf')
    left = 0
    curr_sum = 0
    
    for right in range(n):
        curr_sum += nums[right]
        
        while curr_sum >= s:
            min_len = min(min_len, right - left + 1)
            curr_sum -= nums[left]
            left += 1
    
    return min_len if min_len != float('inf') else 0