class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, k = m - 1, n - 1, (n + m - 1)

        while k >= 0 and j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
                continue
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        