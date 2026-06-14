class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(0, max(len(nums), nums[-1])):
            if i not in nums:
                return i
        return len(nums)