class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = val === undefined ? 0 : val;
        this.left = left === undefined ? null : left;
        this.right = right === undefined ? null : right;
    }
}

function leafSimilar(root1: TreeNode | null, root2: TreeNode | null): boolean {
    return arraysEqual(dfs(root1), dfs(root2));
}

function dfs(node: TreeNode | null): number[] {
    if (node === null) {
        return [];
    }
    if (!node.left && !node.right) {
        return [node.val];
    }
    return dfs(node.left).concat(dfs(node.right));
}
function arraysEqual(arr1: number[], arr2: number[]): boolean {
    if (arr1.length !== arr2.length) {
        return false;
    }
    for (let i = 0; i < arr1.length; i++) {
        if (arr1[i] !== arr2[i]) {
            return false;
        }
    }
    return true;
}
