class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums.sort()
        print(nums)
        res = [[]]
        k = 0
        j = nums[0]
        res[k].append(j)
        for i in range(1, len(nums)):
            if nums[i] == j+1:
                res[k].append(nums[i])
                j = nums[i]
            elif nums[i] == j:
                pass
            else:
                res.append([])
                k += 1
                j = nums[i]
                res[k].append(j)
        x = 0
        print(res)
        for l in res:
            if len(l) > x:
                x = len(l)
        return x