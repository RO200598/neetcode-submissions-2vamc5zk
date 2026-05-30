from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[]
        dp.append(nums[0])

        for n in nums:
            idx=bisect_left(dp,n)

            if idx==len(dp):
                dp.append(n)
            else:
                dp[idx]=n
        return len(dp)