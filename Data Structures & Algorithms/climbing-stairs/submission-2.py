class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(n: int, seen: dict) -> int:
            if n in seen:
                return seen[n]

            if n == 1:
                return 1
            if n == 2:
                return 2

            seen[n] = climb(n - 1, seen) + climb(n - 2, seen)
            return seen[n]

        return climb(n, {})