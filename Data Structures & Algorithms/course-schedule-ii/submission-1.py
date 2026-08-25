class Solution:
    def findOrder(self, nu: int, pr: List[List[int]]) -> List[int]:
        adj={i:[] for i in range(nu)}
        for u,v in pr:
            adj[u].append(v)
        
        output=[]
        cycle,visit=set(),set()

        def dfs(node):
            if node in cycle:
                return False
            if node in visit:
                return True
            
            cycle.add(node)
            for ne in adj[node]:
                if dfs(ne)==False:
                    return False
            cycle.remove(node)
            visit.add(node)
            output.append(node)
            return True
        
        for i in range(nu):
            if dfs(i)==False:
                return []
        return output