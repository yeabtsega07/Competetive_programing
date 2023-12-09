class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dict_ = {idx: s[n] for n, idx in enumerate(indices)}
        return ''.join(dict_[i] for i in range(len(s)))
