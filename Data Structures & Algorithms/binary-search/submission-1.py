class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recursive_search(L: int, R: int) -> int:
            if L > R:
                return -1
            
            mid = (L + R) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return recursive_search(mid + 1, R)
            else:
                return recursive_search(L, mid - 1)
                
        return recursive_search(0, len(nums) - 1)