
def numIdenticalPairs(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    freq = Counter(nums)
    count = sum((n * (n - 1)) // 2 for n in freq.values())
    
    return count
from collections import Counter
