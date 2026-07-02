class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        st = strs[0]
        for i in strs:
            if len(i) < len(st):
                st = st[:len(i)]
            j = 0
            while j < len(st):
                if i[j] != st[j]:
                    st = st[:j]
                j += 1
        return st