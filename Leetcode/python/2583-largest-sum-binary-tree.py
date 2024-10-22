from typing import Optional
from collections import deque
import heapq

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        q = deque([root])
        minHeap = []

        while q:
            levelSum = 0
            for i in range(len(q)):
                node = q.popleft()
                levelSum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            heapq.heappush(minHeap, levelSum)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return -1 if len(minHeap) < k else minHeap[0]
