function minimumSteps(s: string): number {
  let l = 0;
  let res = 0;

  for (let r = 0; r < s.length; r++) {
    if (s[r] === "0") {
      res += r - l;
      l += 1;
    }
  }
  return res;
}
