class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def push(list,n):
            if not list:
                list.append(n)
            elif n > list[-1]:
                list.append(n)
            else:
                for i in range(len(list)):
                    if list[i] >= n:
                        list[i] = n
                        return


            
        stack = []
        maxLen = 0
        for n in nums:
            push(stack,n)
            maxLen = max(maxLen,len(stack))
        return maxLen


        