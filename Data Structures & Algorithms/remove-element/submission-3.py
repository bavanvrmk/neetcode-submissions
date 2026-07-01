class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums) - 1
        while r > l and nums[r] == val:
            r -= 1
        while l < r:
            if nums[l] == val:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                while r > l and nums[r] == val:
                    r -= 1
            if r > l:
                l += 1
        return l + 1 if l > 0 else 0