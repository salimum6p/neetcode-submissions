class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        seen = 0
        current = 0
        for i, v in enumerate(nums):
            if v == val:
                seen += 1
                continue
            nums[current] = v
            current += 1
        return len(nums) - seen
