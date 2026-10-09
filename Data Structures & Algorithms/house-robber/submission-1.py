class Solution:
    def rob(self, nums: List[int]) -> int:
        def robHouse(start: int,seen: dict) -> int:
        
            if start >= len(nums):
                return 0
            if start in seen:
                return seen[start]
            seen[start] =  nums[start] + max(robHouse(start + 2,seen), robHouse(start+3,seen))
            return seen[start]
        return max(robHouse(0,{}),robHouse(1,{}))