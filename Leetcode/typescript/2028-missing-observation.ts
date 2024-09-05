function missingRolls(rolls: number[], mean: number, n: number): number[] {
  const m = rolls.length;
  let nTotal = mean * (n + m) - rolls.reduce((a, b) => a + b, 0);

  if (nTotal < n || nTotal > n * 6) return [];

  let res: number[] = [];
  while (nTotal > 0) {
    const dice = Math.min(nTotal - n + 1, 6);
    res.push(dice);
    nTotal -= dice;
    n -= 1;
  }
  return res;
}
