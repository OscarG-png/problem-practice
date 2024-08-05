function kthDistinct(arr: string[], k: number): string {
  let freqMap = new Map<string, number>();

  for (const s of arr) {
    freqMap.set(s, (freqMap.get(s) ?? 0) + 1);
  }
  for (const [word, count] of freqMap.entries()) {
    if (count === 1) {
      k--;
    }
    if (k <= 0) {
      return word;
    }
  }
  return "";
}
