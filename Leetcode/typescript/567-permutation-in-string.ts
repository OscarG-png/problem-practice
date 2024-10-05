function checkInclusion(s1: string, s2: string): boolean {
  const n1 = s1.length;
  const n2 = s2.length;

  if (n1 > n2) return false;

  const s1Count = new Array(26).fill(0);
  const s2Count = new Array(26).fill(0);

  for (let i = 0; i < n1; i++) {
    s1Count[s1.charCodeAt(i) - "a".charCodeAt(0)] += 1;
    s2Count[s2.charCodeAt(i) - "a".charCodeAt(0)] += 1;
  }

  for (let i = 0; i < n2 - n1; i++) {
    if (arraysEqual(s1Count, s2Count)) {
      return true;
    }
    s2Count[s2.charCodeAt(i) - "a".charCodeAt(0)] -= 1;
    s2Count[s2.charCodeAt(i + n1) - "a".charCodeAt(0)] += 1;
  }
  return arraysEqual(s1Count, s2Count);
}

function arraysEqual(a: number[], b: number[]): boolean {
  for (let i = 0; i < a.length; i++) {
    if (a[i] !== b[i]) return false;
  }
  return true;
}
