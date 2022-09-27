class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for ast in asteroids:
            if ast<=mass:
                mass+=ast
            elif ast>mass:
                return False
                
        return True        
        