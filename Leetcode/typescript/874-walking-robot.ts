function robotSim(commands: number[], obstacles: number[][]): number {
  let x = 0,
    y = 0,
    d = 0;
  const directions = [
    [0, 1], // North
    [1, 0], // East
    [0, -1], // South
    [-1, 0], // West
  ];
  let maxDistance = 0;
  const obs = new Set(obstacles.map((obstacle) => obstacle.toString()));

  for (const cmd of commands) {
    if (cmd === -1) {
      d = (d + 1) % 4;
    } else if (cmd === -2) {
      d = (d + 3) % 4;
    } else {
      for (let i = 0; i < cmd; i++) {
        const nx = x + directions[d][0];
        const ny = y + directions[d][1];
        if (obs.has([nx, ny].toString())) {
          break;
        }
        x = nx;
        y = ny;
        maxDistance = Math.max(maxDistance, x * x + y * y);
      }
    }
  }
  return maxDistance;
}
