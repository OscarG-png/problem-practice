class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        num_freq = {}
        for num in arr:
            num_freq[num] = num_freq.get(num, 0) + 1

        freq_set = set()

        for value in num_freq.values():
            if value in freq_set:
                return False
            else:
                freq_set.add(value)
        return True
