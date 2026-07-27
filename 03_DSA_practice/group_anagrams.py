def group_anagrams(words):
    # Dictionary to map sorted character signatures to lists of anagrams
    sorted_signature = {}

    for word in words:
        # Sort letters of the word to create a unique identifier for anagrams
        signature = "".join(sorted(word))

        # Initialize list if key does not exist, then append current word
        if signature not in sorted_signature:
            sorted_signature[signature] = []
        sorted_signature[signature].append(word)

    # Return grouped words as a list of lists
    return list(sorted_signature.values())


# Complexity Analysis:
# Time Complexity: O(n * k log k) : 'n' is the number of words, 'k' is the maximum length of a word (due to sorting)
# Space Complexity: O(n * k) : Space required to store the grouped strings in the dictionary

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(f"Grouped anagrams: {group_anagrams(words)}")