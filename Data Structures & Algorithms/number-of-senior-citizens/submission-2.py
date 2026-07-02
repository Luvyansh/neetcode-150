class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for d in details:
            age = d[11:13]
            if int(age) > 60: count += 1
        return count