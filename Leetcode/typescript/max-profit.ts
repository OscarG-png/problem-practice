function maxProfit(prices: number[]): number {
  let l = 0;
  let r = 1;
  let profit = 0;

  while (r < prices.length) {
    if (prices[r] < prices[l]) {
      [l, r] = [r, r + 1];
    } else {
      profit = Math.max(profit, prices[r] - prices[l]);
      r += 1;
    }
  }
  return profit;
}
