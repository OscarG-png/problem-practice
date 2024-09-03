function getLucky(s: string, k: number): number {
  let numStr = s
    .split("")
    .map((c) => (c.charCodeAt(0) - 96).toString())
    .join("");

  for (let i = 0; i < k; i++) {
    let sum = 0;
    for (const c of numStr) {
      sum += parseInt(c, 10);
    }
    numStr = sum.toString();
  }
  return parseInt(numStr, 10);
}
