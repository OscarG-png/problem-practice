class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
            hashMap = {
                "first": [],
                "second": []
            }
            nums1_set = set(nums1)
            nums2_set = set(nums2)

            for num in nums1_set:
                if num not in nums2_set:
                    hashMap["first"].append(num)
            for num in nums2_set:
                if num not in nums1_set:
                    hashMap["second"].append(num)

            res = []
            for value in hashMap.values():
                res.append(value)

            return res
