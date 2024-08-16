function maxDistance(arrays: number[][]): number {
  let currMin = arrays[0][0];
  let currMax = arrays[0][arrays[0].length - 1];
  let res = 0;

  for (let i = 1; i < arrays.length; i++) {
    const arr = arrays[i];
    res = Math.max(res, arr[arr.length - 1] - currMin, currMax - arr[0]);
    currMin = Math.min(currMin, arr[0]);
    currMax = Math.max(currMax, arr[arr.length - 1]);
  }
  return res;
}
