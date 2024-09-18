function largestNumber(nums: number[]): string {
    let newNums = nums.map(String);
    newNums.sort((a, b) => {
        if (a + b > b + a) return -1;
        else if (a + b < b + a) return 1;
        return 0;
    });
    if (newNums[0] === "0") return "0";
    return newNums.join("");
}
