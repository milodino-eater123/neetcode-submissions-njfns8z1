class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        def push(lst,n):
            while lst and temperatures[n] >= temperatures[lst[-1]]:
                lst.pop()
            lst.append(n)

        #iterate from back
        for i in range(len(temperatures)-1,-1,-1):
            push(stack,i)
            #if stack has value greater than i, there will be value behind the cur, thus stack must be at least 2 length
            if len(stack) >= 2:
                diff = stack[-2] - stack[-1]
                res[i] = diff

        return res      


        