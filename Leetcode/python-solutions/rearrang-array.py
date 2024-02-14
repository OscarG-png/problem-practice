class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg, result = [], [], []

        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        idx1, idx2 = 0, 0

        while idx2 < len(nums) // 2:
            result.append(pos[idx1])
            idx1 += 1
            result.append(neg[idx2])
            idx2 += 1
        return result
