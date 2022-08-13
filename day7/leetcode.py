class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l=len(nums)+1
        for i in range(l):
            if i not in nums:
                return i
