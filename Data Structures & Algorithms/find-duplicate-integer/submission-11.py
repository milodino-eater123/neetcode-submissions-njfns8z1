class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow1=0
        slow2=nums[slow]
        while slow1!=slow2:
            slow1 = nums[slow1]
            slow2 = nums[slow2]
        return slow1

        