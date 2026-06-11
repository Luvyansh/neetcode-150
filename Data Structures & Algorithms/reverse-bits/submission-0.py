class Solution:
    def reverseBits(self, n: int) -> int:
        a = f"{n:032b}"
        return int(a[::-1], 2)