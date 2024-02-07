class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        res = ''
        for c, f in freq:
            res += c * f
        return res
