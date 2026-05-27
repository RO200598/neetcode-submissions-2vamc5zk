class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.robby(nums[1:]),self.robby(nums[:-1]))
    
    def robby(self,nums):
        rob1,rob2=0,0
        for n in nums:
            new=max(rob1+n,rob2)
            rob1=rob2
            rob2=new
        return rob2