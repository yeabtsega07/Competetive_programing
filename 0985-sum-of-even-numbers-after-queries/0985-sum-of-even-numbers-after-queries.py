class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = [] 
        even = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even[i] = nums[i]
        sum_ = sum(even.values())
        
        for i, query in enumerate(queries):
            pre = nums[query[1]]
            nums[query[1]] += query[0]
            
            if pre % 2 == 0:
                if nums[query[1]] % 2 == 0:
                    sum_ += query[0]
                    even[query[1]] = nums[query[1]]
                else:
                    sum_ -= even[query[1]]
                    even.pop(query[1])
            else:
                if nums[query[1]] % 2 == 0:
                    sum_ += nums[query[1]]
                    even[query[1]] = nums[query[1]]
            
            # print(sum_, nums)
            if sum_ % 2 == 0:
                ans.append(sum_)
                     
            
        return ans