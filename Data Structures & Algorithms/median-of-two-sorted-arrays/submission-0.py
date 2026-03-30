class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) <= len(nums2):
            smaller = nums1
            bigger = nums2
        else:
            smaller = nums2
            bigger = nums1
        
        total = len(nums1) + len(nums2)
        half = total // 2 

        

        low,high = -1, len(smaller)-1
        while high >= low:
            mid = (high+low) // 2
            print(f"mid={mid}, low={low}, high={high}")
            smaller1 = smaller[mid] if mid >= 0 else float('-inf')
            smaller2 = smaller[mid+1] if mid + 1 < len(smaller) else float('inf')
            j = half - mid - 2
            bigger1 = bigger[j] if j >= 0 else float('-inf')
            bigger2 = bigger[j+1] if j+1 < len(bigger) else float('inf')
            print(f"smaller1={smaller1}, smaller2={smaller2}, bigger1={bigger1}, bigger2={bigger2}, j={j}")
            if smaller1 > bigger2:
                high = mid - 1
            elif bigger1 > smaller2:
                low = mid + 1
            else:
                break

        while high >= low:
            mid = (high+low) // 2 
            smaller1 = smaller[mid] if mid >= 0 else float('-inf')
            smaller2 = smaller[mid+1] if mid + 1 <len(smaller) else float('inf')
            j = half - mid - 2 
            bigger1 = bigger[j] if j >= 0 else float('-inf')
            bigger2 = bigger[j+1] if j+1 < len(bigger) else float('inf')
            if smaller1 > bigger2:
                high = mid - 1 
            elif bigger1 > smaller2:
                low = mid + 1 
            else:
                break

        if total % 2 == 1:
            return min(bigger2,smaller2)
        else:
            return (min(bigger2,smaller2) + max(smaller1,bigger1)) / 2 
