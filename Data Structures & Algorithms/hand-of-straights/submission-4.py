from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False

        card_hmap = defaultdict(int)

        for card in hand:
            card_hmap[card]+=1

        hand = sorted(list(set(hand)))

        for card in hand:
            if card not in card_hmap:
                continue
            for i in range(1,groupSize):
                left = card_hmap[card+i] - card_hmap[card]
                if left < 0:
                    return False
                else:
                    card_hmap[card+i] = left
        
        return True
                
        
        