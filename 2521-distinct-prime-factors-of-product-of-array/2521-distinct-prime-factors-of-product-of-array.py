class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        # num = 1
        track = set()

        for num in nums:
            
            prime = 2

            while prime * prime <= num:

                while num % prime == 0:

                    track.add( prime )
                    num = num // prime

                prime += 1

            if num > 1:

                track.add( num )
        
        return len( track )
        