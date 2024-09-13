function xorQueries(arr: number[], queries: number[][]): number[] {
  const prefix: number[] = [0];

  for (const num of arr) {
    prefix.push(prefix[prefix.length - 1] ^ num);
  }

  const res: number[] = [];

  for (const [l, r] of queries) {
    res.push(prefix[r + 1] ^ prefix[l]);
  }
  return res;
}
