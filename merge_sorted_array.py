def merge(nums1, m, nums2, n):
    # Create a new array to store the merged result
    merged = [0] * (m + n)
    
    # Pointers for nums1, nums2, and merged array
    i, j, k = 0, 0, 0
    
    # Merge the arrays by comparing elements
    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            merged[k] = nums1[i]
            i += 1
        else:
            merged[k] = nums2[j]
            j += 1
        k += 1
    
    # Copy remaining elements from nums1, if any
    while i < m:
        merged[k] = nums1[i]
        i += 1
        k += 1
    
    # Copy remaining elements from nums2, if any
    while j < n:
        merged[k] = nums2[j]
        j += 1
        k += 1
    
    # Update nums1 with the merged result
    nums1[:] = merged
