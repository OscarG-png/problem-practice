from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1 = Counter(word1)
        w2 = Counter(word2)

        count1 = Counter([v for v in w1.values()])
        count2 = Counter([v for v in w2.values()])

        return w1 == w2 or (count1 == count2 and set(word1) == set(word2))
