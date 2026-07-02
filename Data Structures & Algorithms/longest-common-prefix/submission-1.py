class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        _min = min(len(s) for s in strs)
        ans = ""
        for i in range(_min):
            curr = strs[0][i]
            for s in strs[1:]:
                if s[i] != curr:
                    return ans
            ans += curr
        return ans