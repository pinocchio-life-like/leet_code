from collections import Counter

def minOperations(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    num_dict = Counter(nums)
    count = 0
    for num in nums:
        v = num_dict[num]
        if v == 1:
            return -1
        quo, rem = divmod(v, 3)
        if rem == 0:
            count += quo
        elif rem == 1 or rem == 2:
            count += quo + 1
        else:
            count += quo + 2
    return count
