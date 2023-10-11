class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        
        len_a = len(a)
        len_b = len(b)
        
        div = len_b // len_a
        
        def is_substring(needle, haystack):
            def KMP_part_one(p : str) -> list:
                m = len(p)
                prevLPS, i = 0, 1
                LPS = [0 for _ in range(m)]
                while i < m:
                    if p[prevLPS] == p[i]:
                        LPS[i] = prevLPS + 1
                        prevLPS += 1
                        i += 1
                    else:
                        if prevLPS == 0:
                            i += 1
                        else:
                            prevLPS = LPS[prevLPS - 1]
                return LPS
        
            lps = KMP_part_one(needle) 
            s_i, n_i = 0, 0

            while s_i < len(haystack):
                if needle[n_i] == haystack[s_i]:
                    s_i += 1
                    n_i += 1
                elif n_i == 0:
                    s_i += 1
                else:
                    n_i = lps[n_i - 1]

                if n_i == len(needle):
                    return s_i - n_i

            return -1
        
        for i in range(div, div + 3):
            if is_substring(b, a * i) != -1:
                return i
        
        return -1
            