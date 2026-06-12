class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = True
        for i in range(len(digits) - 1, -1, -1):
            digit = digits[i]
            if carry:
                digit += 1
            if digit == 10:
                digits[i] = 0
            else:
                digits[i] = digit
                carry = False
        if carry:
            digits = [1] + digits
        return digits