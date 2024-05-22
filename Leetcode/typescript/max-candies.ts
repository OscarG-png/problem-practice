function kidsWithCandies(candies: number[], extraCandies: number): boolean[] {
  const maxCandies = Math.max(...candies);

  return candies.map((candy) => candy + extraCandies >= maxCandies);
}
