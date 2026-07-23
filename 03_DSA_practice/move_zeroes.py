def move_zeroes(numbers):
    # 'slow' tracks the position for the next non-zero element
    slow = 0

    # 'fast' scans through every element in the list
    for fast in range(len(numbers)):
        # When a non-zero element is found, swap it to the 'slow' index
        if numbers[fast] != 0:
            numbers[slow], numbers[fast] = numbers[fast], numbers[slow]
            slow += 1

    return numbers

# Complexity Analysis:
# Time Complexity: O(n) : Single linear pass through the array
# Space Complexity: O(1) : Modifies the array in-place without extra allocation

numbers = [0, 1, 0, 3, 12]
print(f"Moved zeroes to end : {move_zeroes(numbers)}")