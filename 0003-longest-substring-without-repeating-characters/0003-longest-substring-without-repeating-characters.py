class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

       seen = {}
       start = 0
       max_len = 0

       for end in range(len(s)):
           curr_char = s[end]
           if curr_char in seen and seen[curr_char] >= start:
               start = seen[curr_char] + 1
           seen[curr_char] = end
           max_len = max(max_len, end - start + 1)

       return max_len