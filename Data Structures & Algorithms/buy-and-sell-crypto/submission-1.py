class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        b = prices[0]

        for s in prices:
            p = max(p, s - b)
            b = min(b, s)
        return p