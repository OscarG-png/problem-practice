function frequencySort(nums: number[]): number[] {
  let freqMap = new Map();
  nums = nums.sort((a, b) => b - 1);
  for (const num of nums) {
    freqMap.set(num, (freqMap.get(num) || 0) + 1);
  }
  nums.sort((a, b) => {
    let freqA = freqMap.get(a) || 0;
    let freqB = freqMap.get(b) || 0;

    if (freqA === freqB) {
      return b - a;
    } else {
      return freqA - freqB;
    }
  });
  return nums;
}
