class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig=image[sr][sc]
        if orig==color:
            return image
        
        n=len(image)
        m=len(image[0])
        q=deque([(sr,sc)])
        image[sr][sc]=color
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        while q:
            r,c=q.popleft()
            for dr,dc in directions:
                row,col=r+dr,c+dc
                if (row in range(len(image))and
                    col in range(len(image[0]))and
                    image[row][col]==orig):
                    image[row][col]=color
                    q.append((row,col))
        return image

