function isAnagram(s: string, t: string): boolean {
  if (s.length !== t.length) return false;

  const charMap: { [key: string]: number } = {};

  for (let i = 0; i < s.length; i++) {
    charMap[s[i]] = (charMap[s[i]] || 0) + 1;
    charMap[t[i]] = (charMap[t[i]] || 0) - 1;
  }

  for (const c in charMap) {
    if (charMap[c] !== 0) return false;
  }
  return true;
}
