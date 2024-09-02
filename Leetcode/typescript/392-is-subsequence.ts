function isSubsequence(s: string, t: string): boolean {
  if (!s) return true;

  let l = 0;
  let r = 0;
  while (l < s.length && r < t.length) {
    if (s[l] === t[r]) {
      l++;
      if (l == s.length) return true;
    }
    r++;
  }
  return false;
}
