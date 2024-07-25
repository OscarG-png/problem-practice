function sortArray(nums: number[]): number[] {
  // i basically just made merge sort, nothing special

  function mergeSort(arr: number[]) {
    if (arr.length <= 1) {
      return arr;
    }

    const mid = Math.floor(arr.length / 2);

    const leftMerge = mergeSort(arr.slice(0, mid));
    const rightMerge = mergeSort(arr.slice(mid));
    return merge(leftMerge, rightMerge);
  }
  function merge(left, right) {
    let sortedList: number[] = [];
    let leftIndex = 0;
    let rightIndex = 0;

    while (leftIndex < left.length && rightIndex < right.length) {
      if (left[leftIndex] < right[rightIndex]) {
        sortedList.push(left[leftIndex]);
        leftIndex++;
      } else {
        sortedList.push(right[rightIndex]);
        rightIndex++;
      }
    }

    while (leftIndex < left.length) {
      sortedList.push(left[leftIndex]);
      leftIndex++;
    }
    while (rightIndex < right.length) {
      sortedList.push(right[rightIndex]);
      rightIndex++;
    }
    return sortedList;
  }
  return mergeSort(nums);
}
