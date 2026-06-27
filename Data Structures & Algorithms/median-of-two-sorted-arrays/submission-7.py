class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1,l2 = len(nums1),len(nums2)
        if l1+l2==0:
            return None
        if l1<l2:
            l1,l2=l2,l1
            nums1,nums2=nums2,nums1
        low,high = 0,l2
        half = (l1+l2)//2
        while True:
            j = (high+low)//2 if nums2 else -1
            i = half-j-2
            a1 = nums1[i] if 0<=i<l1 else float('-inf')
            a2 = nums1[i+1] if 0<=i+1<l1 else float('inf')
            b1 = nums2[j] if 0<=j<l2 else float('-inf')
            b2 = nums2[j+1] if 0<=j+1<l2 else float('inf')
            if b1>a2:
                high = j-1
            elif a1>b2:
                low = j+1
            else:
                break
        lower1 = nums1[i] if 0<=i<l1 else float('-inf')
        lower2 = nums2[j] if 0<=j<l2 else float('-inf')
        upper1 = nums1[i+1] if 0<=i+1<l1 else float('inf')
        upper2 = nums2[j+1] if 0<=j+1<l2 else float('inf')

        if (l1+l2)%2==0:
            return (max(lower1,lower2)+min(upper1,upper2))/2
        else:
            return (min(upper1,upper2))


        
        