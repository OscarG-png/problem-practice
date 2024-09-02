function chalkReplacer(chalk: number[], k: number): number {
  const total = chalk.reduce((a, b) => a + b, 0);
  const n = chalk.length;

  let left = k % total;
  if (left === 0) return 0;

  for (let i = 0; i < n; i++) {
    left -= chalk[i];
    if (left < 0) return i;
  }
  return -1;
}
