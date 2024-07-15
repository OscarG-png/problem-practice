class NumArray:

    def __init__(self, nums: List[int]):
        self.values = nums

    def sumRange(self, left: int, right: int) -> int:
        res = sum(self.values[left: right + 1])
        return res


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
