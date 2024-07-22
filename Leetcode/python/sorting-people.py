from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        peopleMap = {}

        for i in range(len(names)):
            peopleMap[heights[i]] = names[i]

        sortedHeights = sorted(peopleMap.keys(), reverse=True)
        res = [peopleMap[height] for height in sortedHeights]
        return res
