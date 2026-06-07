class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1,l2 = len(word1),len(word2)
        dp = [] #i+1, 0-(l2-1) j+1 
        for j in range(l2+1):
            dp.append(l2-j)
        for i in range(l1-1,-1,-1):
            placeholder=l1-i-1
            dp[l2]=l1-i
            for j in range(l2-1,-1,-1):
                temp=dp[j]
                if word1[i]==word2[j]:
                    dp[j]=placeholder
                else:
                    dp[j]=1+min(dp[j],dp[j+1],placeholder)
                placeholder=temp
        return dp[0]



          
        

