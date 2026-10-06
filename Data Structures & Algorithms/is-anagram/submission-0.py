class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for l1,l2 in zip(s,t):
            if l1 in count:
                count[l1] += 1
            else:
                count[l1] = 1
            if l2 in count:
                count[l2] -= 1
            else:
                count[l2] = -1
        for i in count.values():
            if i != 0:
                return False
        return True