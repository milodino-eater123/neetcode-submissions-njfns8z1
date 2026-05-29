class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def add(i,total,path):
            if total == target:
                res.append(path.copy())
                return
            if i>=len(candidates):
                return
            if total+candidates[i]>target:
                return

            path.append(candidates[i])
            add(i+1,total+candidates[i],path)
            path.pop()

            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            
                
            add(i+1,total,path)
        add(0,0,[])
        return res
        