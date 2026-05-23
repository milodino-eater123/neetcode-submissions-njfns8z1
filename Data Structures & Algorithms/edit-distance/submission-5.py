class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1,l2 = len(word1),len(word2)
        hmap = {}
        def edit(i,j):
            if i == l1 and j == l2:
                return 0
            
            if (i,j) in hmap:
                return hmap[(i,j)]

            #case 1: word1 c does not exist
            if i == l1:
                return 1 + edit(i,j+1)
            
            #case 2: word2 c does not exist
            if j == l2:
                return 1 + edit(i+1,j)

            #case 3: same
            if word1[i]==word2[j]:
                return edit(i+1,j+1)
           
            #case 4: different
            if word1[i]!=word2[j]:
                res = 1 + min(edit(i,j+1),edit(i+1,j),edit(i+1,j+1))
                hmap[(i,j)] = res
                return res
        
        return edit(0,0)

          
        

