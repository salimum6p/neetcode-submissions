import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]+',"", s)
        for idx in range(len(s)):
            if s[idx].lower() != s[len(s) - idx - 1].lower():
                return False
        return True
