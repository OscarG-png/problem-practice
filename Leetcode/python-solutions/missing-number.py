class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        check = [-1] * (n + 1)

        for num in nums:
            check[num] = num

        for i in range(len(check)):
            if check[i] == -1:
                return i
        return 0
