class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        hashMap = Counter(arr)

        freq = list(hashMap.values())

        freq.sort()

        removedItems = 0

        for i in range(len(freq)):
            removedItems += freq[i]

            if removedItems > k:
                return len(freq) - i
        return 0
