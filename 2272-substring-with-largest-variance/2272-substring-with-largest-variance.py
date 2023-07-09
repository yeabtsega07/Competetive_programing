class Solution:
    def largestVariance(self, s: str) -> int:

        counter = [0] * 26
        for char in s:
            counter[ord(char) - ord('a')] += 1
        max_ = 0

        for i in range(26):
            for j in range(26):
                if i == j or counter[i] == 0 or counter[j] == 0:
                    continue

                max_char = chr(ord('a') + i)
                min_char = chr(ord('a') + j)
                max_cnt = 0
                min_cnt = 0
                rest_min = counter[j]

                for char in s:
                    if char == max_char:
                        max_cnt += 1
                    if char == min_char:
                        min_cnt += 1
                        rest_min -= 1

                    if min_cnt > 0:
                        max_ = max(max_, max_cnt - min_cnt)

                    if max_cnt < min_cnt and rest_min > 0:
                        max_cnt = 0
                        min_cnt = 0

        return max_

        
        