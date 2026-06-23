class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumOfSquares(n)

        while slow != fast:
            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)
            slow = self.sumOfSquares(slow)
        return True if fast == 1 else False



    def sumOfSquares(self, n):
        sum = 0
        while n != 0:
            digit = n % 10
            sum += digit ** 2
            n = n // 10
        return sum