class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size = len(nums)
        res = [0] * 2* size
        for index, num in enumerate(nums):
            res[index] = num
            res[index + size] = num

        return res