class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = temp = 0
        for i in nums:
            if i == 1:
                temp += 1
            count = max(count, temp)
            if i != 1:
                temp = 0
        return count