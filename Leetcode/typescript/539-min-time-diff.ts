function findMinDifference(timePoints: string[]): number {
  timePoints.sort();

  function timeToMin(t: string) {
    const [h, m] = t.split(":").map(Number);
    return 60 * h + m;
  }

  let res =
    24 * 60 -
    timeToMin(timePoints[timePoints.length - 1]) +
    timeToMin(timePoints[0]);
  for (let i = 0; i < timePoints.length - 1; i++) {
    const curr = timeToMin(timePoints[i + 1]);
    const prev = timeToMin(timePoints[i]);
    const diff = curr - prev;
    res = Math.min(res, diff);
  }
  return res;
}
