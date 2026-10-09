class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def coin(start: int, seen: dict) -> int:
            if start == 0:
                return 0
            if start < 0:
                return float('inf')
            if start in seen:
                return seen[start]

            seen[start] = min(
                1 + coin(start - c, seen)
                for c in coins
            )

            return seen[start]

        result = coin(amount, {})

        return result if result != float('inf') else -1