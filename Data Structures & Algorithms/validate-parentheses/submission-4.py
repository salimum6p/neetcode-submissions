class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {')': '(', '}': '{', ']': '['}

        for par in s:
            if par in parentheses:
                if stack and parentheses[par] == stack.pop():
                    continue
                else:
                    return False
            else:
                stack.append(par)

        return not stack