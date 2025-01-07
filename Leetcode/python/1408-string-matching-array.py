from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for word in words:
            for other_word in words:
                if word in other_word and word != other_word:
                    result.append(word)
                    break
        return result
