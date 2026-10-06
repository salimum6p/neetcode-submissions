class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<2:
            return False
        parentheses = {'}': '{', ')': '(', ']': '['}
        stack = []
        for par in s:
            if par in parentheses.values():
                stack.append(par)
                continue
            if not stack or stack.pop() != parentheses[par]:
                return False
        if stack:
            return False
        return True