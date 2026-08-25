class Solution:
    def canFinish(self, nu: int, pr: List[List[int]]) -> bool:
        adj={i: [] for i in range(nu)}
        for u,v in pr:
            adj[u].append(v)

        visit=set()

        def dfs(node):
            if node in visit:
                return False
            if adj[node]==[]:
                return True
            
            visit.add(node)
            for ne in adj[node]:
                if not dfs(ne):
                    return False
            visit.remove(node)
            adj[node]=[]
            return True
        
        for c in range(nu):
            if not dfs(c):
                return False
        return True