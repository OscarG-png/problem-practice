class Solution:
    def minimumPushes(self, word: str) -> int:
        count = [0] * 26

        for c in word:
            count[ord(c) - ord('a')] += 1

        count.sort(reverse=True)

        res = 0
        distinct = 0

        for cnt in count:
            res += cnt * (1 + distinct // 8)
            distinct += 1
        return res
