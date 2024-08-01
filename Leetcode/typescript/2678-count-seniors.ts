function countSeniors(details: string[]): number {
  let res = 0;

  for (const d of details) {
    const age = parseInt(d.slice(11, 13));

    if (age > 60) {
      res++;
    }
  }

  return res;
}
