function sortJumbled(mapping: number[], nums: number[]): number[] {
  let pairs: [number, number][] = [];

  for (let i = 0; i < nums.length; i++) {
    const numStr = `${nums[i]}`;
    let mappedNum = 0;

    for (const c of numStr) {
      mappedNum = mappedNum * 10 + mapping[parseInt(c)];
    }
    pairs.push([mappedNum, i]);
  }
  pairs.sort((a, b) => a[0] - b[0] || a[1] - b[1]);
  return pairs.map((pair) => nums[pair[1]]);
}
