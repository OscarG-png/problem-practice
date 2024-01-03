class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        result = [num for num, _ in sorted_freq[:k]]
        return result
