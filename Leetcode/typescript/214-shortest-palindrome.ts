function shortestPalindrome(s: string): string {
  function isPalindrome(s: string, l: number, r: number): boolean {
    while (l <= r) {
      if (s[l] !== s[r]) return false;
      l++;
      r--;
    }
    return true;
  }
  const n = s.length;
  let r: number;
  for (r = n; r >= 0; r--) {
    if (isPalindrome(s, 0, r)) break;
  }
  const suffix = s.slice(r + 1, n);

  return suffix.split("").reverse().join("") + s;
}
