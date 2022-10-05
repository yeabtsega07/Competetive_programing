class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        if not tokens or power<tokens[0]:
            return 0
        top,rear=0,len(tokens)-1
        score=0
        while top<=rear:
            if power>=tokens[top]:
                power-=tokens[top]
                score+=1
                top+=1
            else:
                if rear-top>1:
                    score-=1
                    power+=tokens[rear]
                    rear-=1
                else:
                    return score

        return score
                
            