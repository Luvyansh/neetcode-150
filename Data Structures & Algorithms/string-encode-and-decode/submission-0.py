class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for i in strs:
            s += '!@!674!.!'+i
        return s

    def decode(self, s: str) -> List[str]:
        return s.split('!@!674!.!')[1:]