function subsets(nums: number[]): number[][] {
  let res: number[][] = [];
  nums.sort((a, b) => a - b);

  let subSet: number[] = [];
  function dfs(i: number) {
    if (i >= nums.length) {
      res.push([...subSet]);
      return;
    }
    subSet.push(nums[i]);
    dfs(i + 1);

    subSet.pop();
    dfs(i + 1);
  }
  dfs(0);
  return res;
}
