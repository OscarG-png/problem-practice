function uncommonFromSentences(s1: string, s2: string): string[] {
  const words = s1.split(" ").concat(s2.split(" "));

  const wordCount = {};

  for (const word of words) {
    wordCount[word] = (wordCount[word] || 0) + 1;
  }
  let res: string[] = [];
  for (const word in wordCount) {
    if (wordCount[word] === 1) {
      res.push(word);
    }
  }
  return res;
}
