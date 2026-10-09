class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        def minClimb(start: int, seen: dict) -> int:
            if start >= len(cost):
                return 0

            if start in seen:
                return seen[start]

            seen[start] = cost[start] + min(
                minClimb(start + 1, seen),
                minClimb(start + 2, seen)
            )

            return seen[start]

        return min(minClimb(0, {}), minClimb(1, {}))