class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        response = ''

        for s in strs:
            response += str(len(s)) + "#" + s
        return response
    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        result = []
        i = 0

        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            result.append(str[j + 1: j + 1 + length])
            i = j + 1 + length
        return result
