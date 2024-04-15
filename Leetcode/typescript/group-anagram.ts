function groupAnagrams(strs: string[]): string[][] {
  let wordMap = new Map();

  for (let word of strs) {
    let sortedWord = word.split("").sort().join("");
    if (!wordMap.has(sortedWord)) {
      wordMap.set(sortedWord, []);
    }
    wordMap.get(sortedWord).push(word);
  }
  return Array.from(wordMap.values()).sort();
}
