function minimumDeletions(s: string): number {
  const n = s.length;
  let aCountRight = 0;

  for (let c of s) {
    if (c === "a") {
      aCountRight++;
    }
  }
  let bCountLeft = 0;
  let res = n;
  for (let i = 0; i < n; i++) {
    if (s[i] === "a") {
      aCountRight--;
    }
    res = Math.min(res, bCountLeft + aCountRight);
    if (s[i] === "b") {
      bCountLeft += 1;
    }
  }
  return res;
}
