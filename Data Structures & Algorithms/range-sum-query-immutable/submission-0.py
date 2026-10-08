class NumArray:

    def __init__(self, nums):
        self.prefix_sum = []
        current = 0
        for v in nums:
            current += v
            self.prefix_sum.append(current)

    def sumRange(self, left, right):
        return self.prefix_sum[right] - (self.prefix_sum[left - 1] if left > 0 else 0)
        


