class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        longest = 0

        for i in nums:
            if i - 1 not in hash_set:
                j = 1
                while i + j in hash_set:
                    j += 1
                longest = max(longest, j)

        return longest