class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[1]*(len(nums)*2)
        l=len(nums)
        for i in range(2*l):
            if i<l:
                ans[i]=nums[i]
            if i>=l:
                ans[i]=nums[i-l]
        return ans
            