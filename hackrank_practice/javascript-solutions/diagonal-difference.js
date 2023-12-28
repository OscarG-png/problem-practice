function diagonalDifference(arr) {
    // Write your code here
    let leftToRight = 0;
    let rightToLeft = 0;

    for (let i = 0; i < arr.length; i++) {
        leftToRight += arr[i][i];
    }
    for (let i = 0; i < arr.length; i ++) {
        rightToLeft += arr[i][(arr.length - 1) - i];
    }
    return Math.abs(leftToRight - rightToLeft);
}


// javascript version on the diagonal difference problem
