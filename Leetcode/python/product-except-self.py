import unittest


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result


class TestSolution(unittest.TestCase):
    def test_product_except_self(self):
        solution = Solution()
        self.assertEqual(solution.productExceptSelf(
            [1, 2, 3, 4]), [24, 12, 8, 6]
        )
        self.assertAlmostEqual(solution.productExceptSelf(
            [-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0]
        )


if __name__ == '__main__':
    unittest.main()
