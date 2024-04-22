function topKFrequent(nums: number[], k: number): number[] {
  let freqMap: Map<number, number> = new Map();

  for (let num of nums) {
    if (!freqMap.has(num)) {
      freqMap.set(num, 0);
    }
    freqMap.set(num, freqMap.get(num)! + 1);
  }
  let res = Array.from(freqMap.keys()).sort(
    (a, b) => freqMap.get(b)! - freqMap.get(a)!,
  );

  return res.slice(0, k);
}
