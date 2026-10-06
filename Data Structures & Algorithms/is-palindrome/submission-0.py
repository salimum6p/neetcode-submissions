import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = s.lower()
        result = re.sub(r'[^a-zA-Z0-9]+',"", text)
        print(result)
        for idx in range(len(result)):
            if result[idx] != result[len(result) - idx - 1]:
                return False
        return True
