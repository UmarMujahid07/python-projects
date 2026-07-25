def reverse_list(numbers):
    # Initialize pointers at the first and last element of the list
    left = 0
    right = len(numbers) - 1

    # Swap elements from outer boundaries toward the center
    while left < right:
        # Tuple unpacking swap to interchange elements in-place
        numbers[left], numbers[right] = numbers[right], numbers[left]

        # Advance left pointer and decrement right pointer
        left += 1
        right -= 1

    return numbers


# Complexity Analysis:
# Time Complexity: O(n) : Iterates through n/2 element pairs
# Space Complexity: O(1) : In-place array modification with zero extra memory overhead

numbers = [1, 3, 4, 5, 8]
print(f"Reversed list is: {reverse_list(numbers)}")