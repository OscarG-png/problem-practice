import unittest


class Solution(object):
    def merge(
            self, nums1, m: int, nums2, n: int
    ):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        elif m == 0:
            nums1 = nums2
            return
        i, j, k = m - 1, n - 1, m + n

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k - 1] = nums1[i]
                i -= 1
            else:
                nums1[k - 1] = nums2[j]
                j -= 1
            k -= 1
        nums1[:j + 1] = nums2[:j + 1]


class TestSolution(unittest.TestCase):
    def test_merge_sorted_arrays(self):
        solution = Solution()
        nums1 = [1, 2, 3, 0, 0, 0]
        nums2 = [2, 5, 6]
        solution.merge(nums1, 3, nums2, 3)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])


if __name__ == '__main__':
    unittest.main()
# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6],
# with the underlined elements coming from nums1.
# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
# Example 3:

# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there
# to ensure the merge result can fit in nums1.
