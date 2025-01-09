from typing import List


class PrefixNode:
    def __init__(self):
        self.children = {}
        self.count = 0


class PrefixTree:
    def __init__(self):
        self.root = PrefixNode()

    def add(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = PrefixNode()
            curr = curr.children[char]
            curr.count += 1

    def count(self, prefix):
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        return curr.count


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        prefix_tree = PrefixTree()

        for word in words:
            if len(word) >= len(pref):
                prefix_tree.add(word)
        return prefix_tree.count(pref)
