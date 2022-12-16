class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = ""
        
        for char in s:
            if char.isalpha() or  char.isdigit():
                check += char.lower()
        
        # print(check)
#         l, r = 0, len(check) - 1
#         while l <= r:
            
#             if check[l] == check[r]:
#                 l += 1
#                 r -= 1
#             else:
#                 return False
#         return True    
        return check == check[::-1]
            
        