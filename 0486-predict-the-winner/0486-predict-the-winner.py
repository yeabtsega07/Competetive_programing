class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
    
        def predict(left, right, score1, score2, turn):
            if left > right:
                return score1 >= score2
            
            if turn:
                Pcase1 = predict(left + 1, right, score1 + nums[left], score2, 0)
                Pcase2 = predict(left, right - 1, score1 + nums[right], score2, 0)
                
                return Pcase1 or Pcase2
            else:
                Pcase1 = predict(left + 1, right, score1, score2 + nums[left], 1)
                Pcase2 = predict(left, right - 1, score1, score2 + nums[right], 1)
                
                return Pcase1 and Pcase2
            
        return predict(0, len(nums)-1, 0, 0, 1) 
        