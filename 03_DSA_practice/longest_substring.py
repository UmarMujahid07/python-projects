def longest_substring(s):
    left = 0
    max_length = 0
    window_chars = set()

    # Expand the window by moving the right pointer
    for right in range(len(s)):
        current_char = s[right]

        # Shrink the window from the left if a duplicate character is found
        while current_char in window_chars:
            window_chars.remove(s[left])
            left += 1

        # Add the unique character to the current window set
        window_chars.add(current_char)

        # Update maximum length found so far
        max_length = max(max_length, right - left + 1)

    return max_length


# Complexity Analysis:
# Time Complexity: O(n) - Each character enters and leaves the set at most once
# Space Complexity: O(min(m, n)) - Space used by set bounded by character set size 'm'

s = "abcabcbb"
print(
    f"Longest sub-string without repeating characters is: {longest_substring(s)}"
)