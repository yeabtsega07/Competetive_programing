class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow,fast,max_=0,0,0
        char={}
        while fast<len(s):
            if s[fast] in char and slow<=char[s[fast]]:
                slow=char[s[fast]]+1
                
            else:
                max_=max(max_,fast-slow+1)
            
            char[s[fast]]=fast 
            fast+=1
        return max_        