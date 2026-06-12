class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        l1,l2 = len(s),len(p)
        def match(i,j):
            return p[j]=="." or s[i]==p[j]
        dp = [False]*(l2) + [True]
        for j in range(l2-1,-1,-1):
            if (l2-j)%2==0:
                dp[j]= dp[j+2] and p[j+1]=='*'
        dp[l2]=False

        for i in range(l1-1,-1,-1):
            prev = i==l1-1
            for j in range(l2-1,-1,-1):
                temp = dp[j]
                if j+1<l2 and p[j+1]=="*":
                    if match(i,j):
                        dp[j]=dp[j] or dp[j+2]
                    else:
                        dp[j]=dp[j+2]
                else:
                    if match(i,j):
                        dp[j]=prev
                    else:
                        dp[j] = False
                prev = temp
        return dp[0]
        