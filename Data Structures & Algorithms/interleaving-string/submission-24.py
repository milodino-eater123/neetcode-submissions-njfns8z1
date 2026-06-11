class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1,l2,l3 = len(s1),len(s2),len(s3)
        if l1+l2 != l3:
            return False
        dp=[True]*(l2+1)
        for i in range(l1,-1,-1):
            for j in range(l2,-1,-1):
                ans = i==l1 and j==l2
                if j<l2 and s2[j]==s3[i+j] and dp[j+1]:
                    ans = True
                if i<l1 and s1[i]==s3[i+j] and dp[j]:
                    ans = True
                dp[j]=ans
        return dp[0]
        