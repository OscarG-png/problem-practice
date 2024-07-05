function groupAnagrams(strs: string[]): string[][] {
  let wordMap: Map<string, string[]> = new Map();

  strs.forEach((str) => {
    const sortedWord = str.split("").sort().join("");
    if (!wordMap.has(sortedWord)) {
      wordMap.set(sortedWord, []);
    }
    wordMap.get(sortedWord)!.push(str);
  });
  return Array.from(wordMap.values());
}
