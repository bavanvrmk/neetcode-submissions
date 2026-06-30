class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        hc=0
        for i in nums:
            if i==1:
                c+=1
            if c>hc:
                hc=c
            if i==0:
                c=0
        return hc