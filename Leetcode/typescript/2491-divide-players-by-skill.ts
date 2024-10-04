function dividePlayers(skill: number[]): number {
  const total = skill.reduce((a, b) => a + b, 0);

  if ((2 * total) % skill.length) return -1;

  const count = {};

  for (const s of skill) {
    count[s] = (count[s] || 0) + 1;
  }
  const target = Math.floor((2 * total) / skill.length);
  let res = 0;

  for (const s of skill) {
    if (!count[s]) continue;

    const diff = target - s;
    if (!count[diff]) return -1;
    res += s * diff;
    count[s]--;
    count[diff]--;
  }
  return res;
}
