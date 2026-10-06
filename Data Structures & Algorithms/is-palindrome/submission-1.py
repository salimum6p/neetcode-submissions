import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = re.sub(r'[^a-zA-Z0-9]+',"", s)
        print(result)
        for idx in range(len(result)):
            if result[idx].lower() != result[len(result) - idx - 1].lower():
                return False
        return True
