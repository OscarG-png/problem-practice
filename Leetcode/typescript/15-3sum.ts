function threeSum(nums: number[]): number[][] {
    nums.sort((a, b) => a - b);
    let res: number[][] = [];

    for (const [i, num] of nums.entries()) {
        if (i > 0 && num == nums[i - 1]) {
            continue;
        }
        let l = i + 1;
        let r = nums.length - 1;
        while (l < r) {
            const curr = num + nums[l] + nums[r];
            if (curr > 0) {
                r--;
            } else if (curr < 0) {
                l++;
            } else {
                res.push([num, nums[l], nums[r]]);
                l++;
                while (nums[l] == nums[l - 1] && l < r) {
                    l++;
                }
            }
        }
    }
    return res;
}
