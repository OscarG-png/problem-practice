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

function goodNodes(root: TreeNode | null): number {
    if (!root) {
        return 0;
    }
    function dfs(node: TreeNode | null, routeMax: number) {
        if (node === null) {
            return 0;
        }
        let currMax = Math.max(routeMax, node.val);
        let val = dfs(node.left, currMax) + dfs(node.right, currMax);
        if (node.val >= currMax) {
            val++;
        }
        return val;
    }
    return dfs(root, root.val);
}
