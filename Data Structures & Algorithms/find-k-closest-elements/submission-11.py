class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #intialise my variables
        low,high = 0,len(arr) - k

        while high > low:
            mid = (high+low)//2
            if abs(arr[mid+k]-x) < abs(arr[mid]-x):
                low = mid + 1
            else:
                high = mid
        
        return(arr[low:low+k])



        #if r + 1 closer than l, low = mid + 1 for l

        #if r + 1 not closer than l , high = mid for l

      


        