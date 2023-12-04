def minWindow(s, t):
    # Initialize a dictionary to store the frequency of characters in t
    target = {}
    for char in t:
        target[char] = target.get(char, 0) + 1

    # Initialize variables to track the minimum window
    left = 0
    min_len = float('inf')
    min_window = ""

    # Initialize a counter to keep track of the characters in t that are present in the current window
    counter = len(t)

    # Iterate over the string s using two pointers, left and right
    for right in range(len(s)):
        # If the current character is in t, decrement the counter
        if s[right] in target:
            target[s[right]] -= 1
            if target[s[right]] >= 0:
                counter -= 1

        # If all characters in t are present in the current window, try to minimize the window
        while counter == 0:
            # Update the minimum window if necessary
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window = s[left:right+1]

            # Move the left pointer to the right to shrink the window
            if s[left] in target:
                target[s[left]] += 1
                if target[s[left]] > 0:
                    counter += 1
            left += 1

    return min_window
