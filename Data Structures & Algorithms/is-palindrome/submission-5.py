class Solution:
    def isValid(self, s: str) -> bool:
        return (
            (ord("A") <= ord(s) <= ord("Z")) or
            (ord("a") <= ord(s) <= ord("z")) or
            (ord("0") <= ord(s) <= ord("9"))
        )

    def isPalindrome(self, s: str) -> bool:
        idx1, idx2 = 0, len(s) - 1
        while idx1 < idx2:
            if not self.isValid(s[idx1]):
                idx1 += 1
                continue
            if not self.isValid(s[idx2]):
                idx2 -= 1
                continue
            if s[idx1].lower() != s[idx2].lower():
                return False
            idx1 += 1
            idx2 -= 1
        return True
        