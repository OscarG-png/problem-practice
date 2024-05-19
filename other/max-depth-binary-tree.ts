/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function maxDepth(root: TreeNode | null): number {
  if (!root) {
    return 0;
  }
  let stack: [TreeNode, number][] = [[root, 1]];
  let maxDepth: number = 0;

  while (stack.length > 0) {
    const nodeDepthPair = stack.pop();
    if (nodeDepthPair) {
      const [curr, depth] = nodeDepthPair;
      maxDepth = Math.max(maxDepth, depth);

      if (curr.left) {
        stack.push([curr.left, depth + 1]);
      }
      if (curr.right) {
        stack.push([curr.right, depth + 1]);
      }
    }
  }
  return maxDepth;
}
