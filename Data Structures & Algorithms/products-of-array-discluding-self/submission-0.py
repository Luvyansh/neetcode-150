class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            temp = nums.copy()
            temp.pop(i)
            res.append(math.prod(temp))
        return res