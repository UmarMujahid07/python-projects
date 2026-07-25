def is_palindrome(word):
    # Initialize pointers at the start and end of the string
    left = 0
    right = len(word) - 1

    # Move pointers toward the center until they meet
    while left < right:
        # If characters at opposite ends do not match, it is not a palindrome
        if word[left] != word[right]:
            return False

        # Move left pointer rightward and right pointer leftward
        left += 1
        right -= 1

    # All corresponding characters matched
    return True


# Complexity Analysis:
# Time Complexity: O(n) : Single pass checking at most n/2 character pairs
# Space Complexity: O(1) : Constant space using two index pointers

word = input("Enter a word: ")

if is_palindrome(word):
    print(f"'{word}' is a palindrome")
else:
    print(f"'{word}' is not a palindrome")