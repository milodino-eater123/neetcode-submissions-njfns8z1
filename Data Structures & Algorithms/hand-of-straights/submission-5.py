from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False

        hmap = defaultdict(int)
        for n in hand:
            hmap[n]+=1
        hand.sort()
        print(hand)
        for n in hand:
            if hmap[n]==0:
                continue
            for i in range(0,groupSize):
                hmap[n+i]-=1
                if hmap[n+i] < 0:
                    print(n,i)
                    return False
        
        return True
        

                
        
        