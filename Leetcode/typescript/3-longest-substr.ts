function lengthOfLongestSubstring(s: string): number {
  let charSet = new Set();
  let l = 0;
  let res = 0;

  for (const r of s) {
    while (charSet.has(s[r])) {
      charSet.delete(s[l]);
      l += 1;
    }
    charSet.add(s[r]);
    res = Math.max(res, r - l + 1);
  }
  return res;
}