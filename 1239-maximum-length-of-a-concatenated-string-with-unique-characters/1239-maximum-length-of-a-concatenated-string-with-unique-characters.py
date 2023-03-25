class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        subs = []
        
        def subsets ( nums ,index = 0, current = [] ):
            
            if index >= len(nums):
                subs.append(current[:])
                return
            
            current.append(nums[index])
            subsets(nums, index + 1, current)
            current.pop()
            
            subsets(nums, index + 1, current)
            
        subsets( arr ) 
        result = 0
        
        for sub in subs:
            
            check = defaultdict(int)
            cur = 0

            for word in sub:
                flag  = True
                for char in word:

                    if check[char]:
                        cur = 0
                        flag = False
                        break
                    else:
                        check[char] += 1
                        cur += 1
                        
                if not flag:
                    cur = 0
                    break
        
            result = max(result, cur)
        
        return result
                