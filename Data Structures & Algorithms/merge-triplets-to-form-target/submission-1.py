class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        #initialise
        foundFirst = foundSecond = foundThird = False
        
        #iterate
        for triplet in triplets:
            #if any triplet value>target, triplet is unusable
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue

            #check usable triplets for any of the numbers needed
            if triplet[0] == target[0]:
                foundFirst = True
            if triplet[1] == target[1]:
                foundSecond = True
            if triplet[2] == target[2]:
                foundThird = True
            
            if foundFirst and foundSecond and foundThird:
                return True
        
        return False
