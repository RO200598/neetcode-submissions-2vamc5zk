class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=nums[0]
        curmin,curmax=1,1

        for n in nums:
            tmp=curmax*n
            curmax=max(n*curmax,n*curmin,n)
            curmin=min(tmp,n*curmin,n)
            res=max(res,curmin,curmax)
        return res