class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #binary search to find x in arr
        low,high = 0,len(arr)-1
        while high > low:
            mid = math.ceil((high+low)/2)
            if x == arr[mid]:
                low = high = mid
            elif x > arr[mid]:
                low = mid
            else:
                high = mid - 1  
        
        found = low
        print(found)
        

        l,r = found, found+1
        
        while l >= 0 and r < len(arr) and r-l-1 < k:
            if x - arr[l] <= arr[r]-x: 
                l -= 1 
            else:
                r += 1 
        
        if l < 0:
            while r-l-1 < k:
               r += 1 
        elif r >= len(arr):
            while r-l-1 < k:
               l -= 1 
        
  
        return arr[l+1:r]
        
        #time complexity: O(max(log(n),k))
        #space complexity: O(k)

      


        