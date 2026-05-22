# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        q=deque([root])

        while q:
            ryt=None
            qlen=len(q)
            for i in range(qlen):
                node=q.popleft()
                if node:
                    ryt=node
                    q.append(node.left)
                    q.append(node.right)
            if ryt:
                res.append(ryt.val)
        return res