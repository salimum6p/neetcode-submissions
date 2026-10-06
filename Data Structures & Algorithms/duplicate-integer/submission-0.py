class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_num = set(nums)
        return not(len(set_num) == len(nums))