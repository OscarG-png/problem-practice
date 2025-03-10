from collections import defaultdict


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:

        def atLeastK(k):
            vowels = defaultdict(int)
            nonVowels = 0
            res = 0
            l = 0
            for r in range(len(word)):
                if word[r] in 'aeiou':
                    vowels[word[r]] += 1
                else:
                    nonVowels += 1
                while len(vowels) == 5 and nonVowels >= k:
                    res += (len(word) - r)
                    if word[l] in 'aeiou':
                        vowels[word[l]] -= 1
                    else:
                        nonVowels -= 1
                    if vowels[word[l]] == 0:
                        vowels.pop(word[l])
                    l += 1
            return res

        return atLeastK(k) - atLeastK(k + 1)
