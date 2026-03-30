from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        #map frequencies to hmap
        hmap = defaultdict(int)
        for n in hand:
            hmap[n] += 1
        
        #convert hand to unique ordered list
        hand = list(set(hand))
        hand.sort()
        
        for i,n in enumerate(hand):
            if hmap[n] == 0:
                continue
            if i >= len(hand) - groupSize + 1:
                return False
            freq = hmap[n]
            for j in range(1,groupSize):
                hmap[n+j] -= freq
                if hmap[n+j] < 0:
                    return False
        
        return True
        


        


        