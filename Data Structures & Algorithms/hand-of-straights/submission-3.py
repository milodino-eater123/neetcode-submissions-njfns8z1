from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
            
        hmap = defaultdict(int)
        for n in hand:
            hmap[n] += 1
        
        hand = list(set(hand))
        hand.sort()

        for n in hand:
            freq = hmap[n]       
            for i in range(1,groupSize):
                hmap[n+i] -= freq
                if hmap[n+i] < 0:
                    return False
        
        return True
        

        