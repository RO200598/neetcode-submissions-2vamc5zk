class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(r,c):
            if (r<0 or c<0 or r==n or c==m or not grid[r][c] or (r,c)in visit):
                return 0
            visit.add((r,c))
            res=1
            for dr,dc in directions:
                res+=dfs(r+dr,c+dc)
            return res
        visit=set()
        land=0
        borderLand=0
        for r in range(n):
            for c in range(m):
                land += grid[r][c]
                if (grid[r][c]and (r,c)not in visit and 
                    (c in [0,m-1]or r in [0,n-1])):
                    borderLand += dfs(r,c)
        
        return land-borderLand