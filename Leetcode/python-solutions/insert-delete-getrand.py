class RandomizedSet:

    def __init__(self):
        self.value = set()

    def insert(self, val: int) -> bool:
        if val in self.value:
            return False
        else:
            self.value.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.value:
            self.value.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        n = len(self.value) - 1
        i = random.randint(0, n)
        return list(self.value)[i]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
