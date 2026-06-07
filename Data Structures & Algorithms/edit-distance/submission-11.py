class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1,l2 = len(word1),len(word2)
        dp = [] 
        for j in range(l2+1):
            dp.append(l2-j)
        for i in range(l1-1,-1,-1):
            placeholder=dp[l2]
            dp[l2]+=1
            for j in range(l2-1,-1,-1):
                temp=dp[j]
                if word1[i]==word2[j]:
                    dp[j]=placeholder
                else:
                    dp[j]=1+min(dp[j],dp[j+1],placeholder)
                placeholder=temp
        return dp[0]



          
        

