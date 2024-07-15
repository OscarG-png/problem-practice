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

function createBinaryTree(descriptions: number[][]): TreeNode | null {
  let nodes: Record<number, TreeNode> = {};
  let children = new Set<number>();

  for (const [parent, child, isLeft] of descriptions) {
    children.add(child);
    if (!nodes[parent]) {
      nodes[parent] = new TreeNode(parent);
    }
    if (!nodes[child]) {
      nodes[child] = new TreeNode(child);
    }
  }
  return null;
}
