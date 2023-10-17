class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        
        wanted =  set()
        unhappy = [0] * n
        
        for pair in pairs:

            for pref in preferences[pair[0]]:

                if pref == pair[1]:
                    break

                if (pair[0], pref) in wanted:
                    unhappy[pair[0]] = 1
                    unhappy[pref] = 1
                else:
                    wanted.add((pref, pair[0]))
                
            for pref in preferences[pair[1]]:

                if pref == pair[0]:
                    break

                if (pair[1], pref) in wanted:
                    unhappy[pair[1]] = 1
                    unhappy[pref] = 1
                else:
                    wanted.add((pref, pair[1]))
        
        return sum(unhappy)
                