from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #adj_list
        links = defaultdict(list)
        for first,second in edges:
            links[first].append(second)
            links[second].append(first)

        hset= { 0 }

        #dfs to check for cycles
        def dfs(cur,prev=None):
            
            for i in links[cur]:
                if i in hset:
                    if i != prev or i == cur:
                        return False
                    else:
                        continue
                hset.add(i)
                if dfs(i,cur) == False:
                    return False

        if dfs(0) == False:
            return False

        #iterate n nodes to check for disconnected nodes
        for i in range(n):
            if i not in hset:
                return False

        return True

        #loop through all nodes, if any node not in set(), false(condition 2)
