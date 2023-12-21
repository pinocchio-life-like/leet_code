def jump(nums):
    if len(nums) <= 1:
        return 0

    jumps = 1
    curr_end = nums[0]
    curr_max = nums[0]

    for i in range(1, len(nums)):
        if i > curr_max:
            return -1

        if i > curr_end:
            jumps += 1
            curr_end = curr_max

        curr_max = max(curr_max, i + nums[i])
    return jumps
