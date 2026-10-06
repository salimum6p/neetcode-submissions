class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for l1,l2 in zip(s,t):
            count[l1] = count.get(l1, 0) + 1
            count[l2] = count.get(l2, 0) - 1
        for i in count.values():
            if i != 0:
                return False
        return True