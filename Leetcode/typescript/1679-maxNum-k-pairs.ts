function maxOperations(nums: number[], k: number): number {
    nums.sort((a, b) => a - b);
    let l = 0;
    let r = nums.length;
    let res = 0;

    while (l < r) {
        const curr = nums[l] + nums[r];
        if (curr == k) {
            res++;
            l++;
            r--;
        } else if (curr < k) {
            l++;
        } else {
            r--;
        }
    }
    return res;
}
