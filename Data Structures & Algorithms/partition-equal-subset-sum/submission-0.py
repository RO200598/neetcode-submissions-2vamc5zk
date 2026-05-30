class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        trgt=sum(nums)//2
        dp=set()
        dp.add(0)

        for i in range(len(nums)):
            nxtdp=set()
            for t in dp:
                nxtdp.add(t+nums[i])
                nxtdp.add(t)
            dp=nxtdp
        return True if trgt in dp else False
                