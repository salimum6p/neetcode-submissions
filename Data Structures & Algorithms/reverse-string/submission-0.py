class Solution:
    def reverseString(self, s: List[str]) -> None:
        def recReverse(s:List[str]) -> List[str]:
            if len(s) == 1:
                return s
            split = int(len(s)/2)
            return (recReverse(s[split:]) + recReverse(s[:split])) 
        s[:] = recReverse(s)

        