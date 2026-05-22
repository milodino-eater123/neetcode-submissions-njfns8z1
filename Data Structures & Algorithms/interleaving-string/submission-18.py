class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1,l2,l3=len(s1),len(s2),len(s3)
        if l1<l2:
            s1,s2 = s2,s1
            l1,l2=l2,l1
        if l1+l2!=l3:
            return False

        dp = [False]*(l2+1)
        dp[l2]=True

        for i in range(l1,-1,-1):
            nextDP = [False]*(l2+1)
            if i==l1:
                nextDP[l2]= True
            for j in range(l2,-1,-1):
                if i<l1 and dp[j] and s1[i]==s3[i+j]:
                    nextDP[j]=True
                if j<l2 and nextDP[j+1] and s2[j]==s3[i+j]:
                    nextDP[j]=True
            dp = nextDP
        
        return dp[0]
        



        