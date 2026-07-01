class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in details:
            if len(i) == 15:
                if int(i[11:13]) > 60:
                    count += 1
        return count