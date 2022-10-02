class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        o(n^2)
        [1,2,3,4]
        
        nums=[1,2,3,4]
        0,1,2,3
        0 2*3*4=24
        ans=[24,12,8,6]
        use prefix and suffix mul
        pre=[1,2,6,24]
        suf=[24,24,12,4]
        0  -->suf[0+1] 24
        1 -->pre[1-1]*suf[1+1] 1*12 = 12
        2 --> pre[2-1]*suf[2+1] 2*4 =8
        4 --> pre[4-1] since 4 is the last index we can't = 6
        time complexity O(n)
        space complexity O(n)
        '''
        n=len(nums)
        suf=[1]*n
        suf[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            suf[i]=suf[i+1]*nums[i]
            
        pre=[1]*n
        pre[0]=nums[0]
        for i in range(1,n):
            pre[i]=pre[i-1]*nums[i]
        for i in range(n):
            if i==0:
                nums[i]=suf[i+1]
            elif i==n-1:
                nums[i]=pre[i-1]
            else:
                nums[i]=pre[i-1]*suf[i+1]
        return nums
        
        
        