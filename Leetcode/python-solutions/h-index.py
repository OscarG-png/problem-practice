class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        h_index = 0
        citations.sort(reverse=True)
        for i, citation in enumerate(citations, start=1):
            if i <= citation:
                h_index = i
            else:
                break
        return h_index
