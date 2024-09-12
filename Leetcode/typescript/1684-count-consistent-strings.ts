function countConsistentStrings(allowed: string, words: string[]): number {
  const allowedSet = new Set(allowed);
  let res = 0;

  for (const word of words) {
    if ([...word].every((char) => allowedSet.has(char))) {
      res++;
    }
  }
  return res;
}
