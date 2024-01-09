class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)

# I didn't think this solution would work but the runtime is pretty slow
# at least the memory usage is middle of the road.
