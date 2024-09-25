class PrefixNode {
  children: (PrefixNode | null)[];
  count: number;

  constructor() {
    this.children = new Array(26).fill(null);
    this.count = 0;
  }
}

class PrefixTree {
  root: PrefixNode;

  constructor() {
    this.root = new PrefixNode();
  }

  insert(word: string): void {
    let curr = this.root;
    for (const c of word) {
      const i = c.charCodeAt(0) - "a".charCodeAt(0);
      if (!curr.children[i]) {
        curr.children[i] = new PrefixNode();
      }
      curr = curr.children[i];
      curr.count++;
    }
  }
  getScore(word: string): number {
    let curr = this.root;
    let score = 0;
    for (const c of word) {
      const i = c.charCodeAt(0) - "a".charCodeAt(0);
      curr = curr.children[i];
      score += curr.count;
    }
    return score;
  }
}

function sumPrefixScores(words: string[]): number[] {
  const res = [];
  const prefixTree = new PrefixTree();

  for (const w of words) {
    prefixTree.insert(w);
  }

  for (const w of words) {
    res.push(prefixTree.getScore(w));
  }
  return res;
}
