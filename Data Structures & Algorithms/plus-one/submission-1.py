class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = False
        res = []
        for i in range((len(digits)-1), -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            if digits[i] == 9:
                if i == 0:
                    digits[i] = 0
                    digits.insert(0, 1)
                    return digits
                digits[i] = 0