function minSwaps(s: string): number {
  let close = 0;
  let maxClose = 0;

  for (const c of s) {
    if (c === "[") {
      close--;
    } else {
      close++;
    }
    maxClose = Math.max(maxClose, close);
  }
  return Math.floor((maxClose + 1) / 2);
}
