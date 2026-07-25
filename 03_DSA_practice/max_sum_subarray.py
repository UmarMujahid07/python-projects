def max_sum_window(numbers, k):
    # Calculate the initial sum of the first window of size k
    window_sum = sum(numbers[0:k])
    max_sum = window_sum

    # Slide the window across the array from index k to the end
    for i in range(k, len(numbers)):
        # Add the incoming element and subtract the outgoing element
        window_sum += numbers[i] - numbers[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


# Complexity Analysis:
# Time Complexity: O(n) : Single linear pass over the array
# Space Complexity: O(1) : Constant auxiliary space used

numbers = [4, 2, 1, 6, 3]
k = 2
result = max_sum_window(numbers, k)
print(f"Max sum is: {result}")