class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:

        # Create a dictionary to map characters in the pattern to words
        chartoword = {}
        # Create a set to store the words we have seen so far
        seenwords = set()
        # Split the string into a list of words
        words = string.split()

        # If the pattern and the list of words have different lengths,
        # then they cannot match
        if len(pattern) != len(words):
            return False

        # Iterate through the characters in the pattern
        for i, char in enumerate(pattern):
            # If the character is not in the mapping yet,
            # add it and the corresponding word to the mapping
            if char not in chartoword:
                chartoword[char] = words[i]
                # If the word has already been added to the mapping,
                # then this pattern is invalid
                if words[i] in seenwords:
                    return False
                seenwords.add(words[i])
            # If the character is in the mapping,
            # but it maps to a different word, then this pattern is invalid
            elif chartoword[char] != words[i]:
                return False

        # If we have not returned False yet, then the pattern is valid
        return True