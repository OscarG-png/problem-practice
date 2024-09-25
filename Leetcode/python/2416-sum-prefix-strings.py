from typing import List


class PrefixNode:
    def __init__(self):
        self.children = [None] * 26
        self.count = 0


class PrefixTree:
    def __init__(self):
        self.root = PrefixNode()

    def insert(self, w):
        curr = self.root
        for c in w:
            i = ord(c) - ord('a')
            if not curr.children[i]:
                curr.children[i] = PrefixNode()
            curr = curr.children[i]
            curr.count += 1

    def getScore(self, w):
        curr = self.root
        score = 0
        for c in w:
            i = ord(c) - ord('a')
            curr = curr.children[i]
            score += curr.count
        return score


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        res = []
        prefixTree = PrefixTree()

        for w in words:
            prefixTree.insert(w)

        for w in words:
            res.append(prefixTree.getScore(w))

        return res
