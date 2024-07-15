class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))

            if sorted_word in result:
                result[sorted_word].append(word)
            else:
                result[sorted_word] = [word]
        result = list(result.values())

        return result
