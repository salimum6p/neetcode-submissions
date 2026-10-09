
from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        out = []

        for right in range(len(nums)):
            while window and nums[window[-1]] < nums[right]:
                window.pop()

            window.append(right)

            if window[0] <= right - k:
                window.popleft()

            if right >= k - 1:
                out.append(nums[window[0]])

        return out
