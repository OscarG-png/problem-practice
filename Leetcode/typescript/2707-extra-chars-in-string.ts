function minExtraChar(s: string, dictionary: string[]): number {
  const words = new Set(dictionary);
  const dp = new Map<number, number>();

  function dfs(i: number) {
    if (i === s.length) return 0;
    if (dp.has(i)) return dp[i];

    let res = 1 + dfs(i + 1);

    for (let j = i; j < s.length; j++) {
      if (words.has(s.slice(i, j + 1))) {
        res = Math.min(res, dfs(j + 1));
      }
    }
    dp[i] = res;
    return res;
  }
  return dfs(0);
}
