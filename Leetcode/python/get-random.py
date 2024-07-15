import random


class RandomizedSet(object):

    def __init__(self):
        self.elements = []
        self.index_map = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.index_map:
            return False
        self.elements.append(val)
        self.index_map[val] = len(self.elements) - 1
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.index_map:
            return False
        index = self.index_map[val]
        self.elements[index], self.elements[-1] = self.elements[-1], self.elements[index]
        self.index_map[self.elements[index]] = index
        self.elements.pop()
        del self.index_map[val]
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        random_index = random.randint(0, len(self.elements) - 1)
        return self.elements[random_index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
