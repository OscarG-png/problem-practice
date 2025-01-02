from typing import List


class Solution:
    def vowelStrings(
            self,
            words: List[str],
            queries: List[List[int]]) -> List[int]:
        vowels = set('aeiou')

        prefixCount = [0] * (len(words) + 1)
        prev = 0

        for i, w in enumerate(words):
            if w[0] in vowels and w[-1] in vowels:
                prev += 1
            prefixCount[i + 1] = prev

        res = [0] * len(queries)

        for i, q in enumerate(queries):
            l, r = q
            res[i] = prefixCount[r + 1] - prefixCount[l]

        return res
