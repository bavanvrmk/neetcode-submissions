class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum=0
        maxsum=nums[0]
        for i in nums:
            cursum=max(cursum,0)+i
            maxsum=max(cursum,maxsum)
        return maxsum