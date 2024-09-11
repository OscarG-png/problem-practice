function minBitFlips(start: number, goal: number): number {
  let startNum = start.toString(2);
  let endNum = goal.toString(2);
  const maxLen = Math.max(startNum.length, endNum.length);

  startNum = startNum.padStart(maxLen, "0");
  endNum = endNum.padStart(maxLen, "0");

  let res = 0;

  for (let i = 0; i < maxLen; i++) {
    if (startNum[i] !== endNum[i]) {
      res++;
    }
  }
  return res;
}
