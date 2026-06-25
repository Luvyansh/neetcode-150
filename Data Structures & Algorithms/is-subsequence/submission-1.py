class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)>len(t):
            return False
        i, j = 0, 0
        for j in range(len(t)):
            if i >= len(s):
                return True
            print(s[i], "==", t[j], "  : ", s[i] == t[j])
            if s[i] == t[j]:
                i +=1
        if i == len(s):
            return True
        return False