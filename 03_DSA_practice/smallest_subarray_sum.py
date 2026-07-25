def smallest_subarray(numbers, target):
    left = 0
    current_sum = 0
    min_length = float("inf")

    # Expand the window by moving the right pointer
    for right in range(len(numbers)):
        current_sum += numbers[right]

        # Shrink the window from the left as long as the target sum condition is met
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= numbers[left]
            left += 1

    # Return 0 if no valid subarray is found
    return min_length if min_length != float("inf") else 0


# Complexity Analysis:
# Time Complexity: O(n) : Each element is added and removed at most once
# Space Complexity: O(1) : In-place tracking variables

numbers = [2, 1, 5, 2, 3, 2]
target = 7
print(f"Minimum subarray is: {smallest_subarray(numbers, target)}")