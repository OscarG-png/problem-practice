from collections import Counter, defaultdict
from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count_2 = defaultdict(int)

        for word in words2:
            count_w = Counter(word)
            for char, count in count_w.items():
                count_2[char] = max(count_2[char], count)

        res = []
        for word in words1:
            count_w = Counter(word)
            flag = True
            for char, count in count_2.items():
                if count_w[char] < count:
                    flag = False
                    break
            if flag:
                res.append(word)
        return res
