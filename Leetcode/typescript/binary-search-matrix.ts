function searchMatrix(matrix: number[][], target: number): boolean {
  const rows = matrix.length;
  const cols = matrix[0].length;
  let top = 0;
  let bot = rows - 1;

  while (top <= bot) {
    const row = Math.floor((top + bot) / 2);
    if (target > matrix[row][matrix[0].length - 1]) {
      top = row + 1;
    } else if (target < matrix[row][0]) {
      bot = row - 1;
    } else {
      return binarySearch(matrix[row], target);
    }
  }

  return false;
}

function binarySearch(arr: number[], target: number): boolean {
  let l = 0;
  let r = arr.length - 1;

  while (l <= r) {
    const mid = Math.floor((l + r) / 2);
    if (arr[mid] < target) {
      l = mid + 1;
    } else if (arr[mid] > target) {
      r = mid - 1;
    } else {
      return true;
    }
  }
  return false;
}
