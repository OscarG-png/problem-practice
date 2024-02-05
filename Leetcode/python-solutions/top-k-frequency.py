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

# alternate solution
        # count = {}
        # freq = [[] for i in range(len(nums) + 1)]

        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)
        # for n, c in count.items():
        #     freq[c].append(n)
        # result = []
        # for i in range(len(freq) -1, 0, -1):
        #     for n in freq[i]:
        #         result.append(n)
        #         if len(result) == k:
        #             return result
