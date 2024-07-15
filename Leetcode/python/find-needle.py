class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # first solution
        # I didn't think this solution would work but
        # the runtime is pretty slow
        # at least the memory usage is middle of the road.
        # return haystack.find(needle)

        # second solution
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1

# This solution is a lot faster on runtime but uses more memory.
