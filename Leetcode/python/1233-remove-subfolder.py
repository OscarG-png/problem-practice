from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folderSet = set(folder)
        res = []

        for f in folder:
            res.append(f)
            for i in range(len(f)):
                if f[i] == "/" and f[:i] in folderSet:
                    res.pop()
                    break

        return res
