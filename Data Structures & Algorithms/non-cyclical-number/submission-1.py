class Solution:
    def isHappy(self, n: int) -> bool:
        Sum = 0
        val = set()
        while True:
            i = n%10
            Sum = Sum + (i**2)
            n = int(n/10)
            if n == 0:
                if Sum in val and Sum != 1:
                    return False
                if Sum == 1:
                    return True
                val.add(Sum)
                n = Sum
                Sum = 0