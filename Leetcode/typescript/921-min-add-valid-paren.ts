function minAddToMakeValid(s: string): number {
  let openCount = 0;
  let res = 0;

  for (const c of s) {
    if (c === "(") {
      openCount++;
    } else {
      if (openCount === 0) res++;
      openCount = Math.max(openCount - 1, 0);
    }
  }
  return res + openCount;
}
