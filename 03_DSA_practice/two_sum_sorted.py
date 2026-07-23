def two_sum_sorted(numbers, target):
    # Two-pointer approach — works only because 'numbers' is sorted
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            return [left,right] # match found, return both indices
        elif current_sum < target:
            left += 1 # sum too small, move left pointer right to increase sum
        else:
            right -= 1 ## sum too big, move right pointer left to decrease sum
    
    return []# no pair found

# Time Complexity: O(n) : single pass, each pointer moves at most n times total
# Space Complexity: O(1) : no extra data structures used
numbers = [1,3,5,7,9,11]
target = 12
print(f"Target found at index {two_sum_sorted(numbers,target)}")