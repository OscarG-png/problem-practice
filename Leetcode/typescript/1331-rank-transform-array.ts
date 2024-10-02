function arrayRankTransform(arr: number[]): number[] {
  const sortedArr = Array.from(new Set(arr)).sort((a, b) => a - b);
  const numMap: { [key: number]: number } = {};

  for (let i = 0; i < sortedArr.length; i++) {
    numMap[sortedArr[i]] = i + 1;
  }

  for (let i = 0; i < arr.length; i++) {
    arr[i] = numMap[arr[i]];
  }
  return arr;
}
