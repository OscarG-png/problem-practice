class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # first solution
        # works but the runtime and memory usages are midway
        # return sorted(s) == sorted(t)

        # second solution

        if len(s) != len(t):
            return False
        char_map = [0] * 26

        for i in range(len(s)):
            char_map[ord(s[i]) - ord('a')] += 1
            char_map[ord(t[i]) - ord('a')] -= 1

        return all(count == 0 for count in char_map)

        # a lot faster on runtime, can't seem to find a way
        # to reduce memory usage
