class Solution:
    def isValid(self, s: str) -> bool:
        pair = {')':'(', ']':'[', '}':'{'}
        stack = deque()
        for i in s:
            if i in pair:
                if stack and stack[-1] == pair[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False