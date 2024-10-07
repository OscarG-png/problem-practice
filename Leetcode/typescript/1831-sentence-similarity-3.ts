function areSentencesSimilar(sentence1: string, sentence2: string): boolean {
  let words1 = sentence1.split(" ");
  let words2 = sentence2.split(" ");

  if (words1.length > words2.length) {
    [words1, words2] = [words2, words1];
  }

  let i = 0;
  while (i < words1.length && words1[i] === words2[i]) {
    i++;
  }

  let j = 0;
  while (
    j < words1.length &&
    words1[words1.length - (j + 1)] === words2[words2.length - (j + 1)]
  ) {
    j++;
  }

  return i + j >= words1.length;
}
