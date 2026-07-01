class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c=0
        d=[]
        for i in range(len(nums)):
            if nums[i]!=val:
                d.append(nums[i])
                c+=1
        nums[:]=d
        return c