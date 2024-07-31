from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        cache = {}

        def helper(i):
            if i == len(books):
                return 0
            if i in cache:
                return cache[i]

            currWidth = shelfWidth
            maxHeight = 0
            cache[i] = float('inf')
            for j in range(i, len(books)):
                width, height = books[j]
                if currWidth < width:
                    break
                currWidth -= width
                maxHeight = max(maxHeight, height)
                cache[i] = min(
                    cache[i],
                    helper(j + 1) + maxHeight
                )
            return cache[i]
        return helper(0)
