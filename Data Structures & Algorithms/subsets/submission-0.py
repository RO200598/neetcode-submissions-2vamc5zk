class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        sbst=[]

        def dfs(i):
            if i>=len(nums):
                res.append(sbst.copy())
                return

            sbst.append(nums[i])
            dfs(i+1)
            sbst.pop()
            dfs(i+1)
        dfs(0)
        return res