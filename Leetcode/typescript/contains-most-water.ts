function maxArea(height: number[]): number {
  let l = 0;
  let r = height.length - 1;
  let maxWater = 0;

  while (l < r) {
    const h = Math.min(height[l], height[r]);
    const w = r - l;
    const area = h * w;
    maxWater = Math.max(maxWater, area);

    if (height[l] < height[r]) {
      l++;
    } else {
      r--;
    }
    return maxWater;
  }
}
