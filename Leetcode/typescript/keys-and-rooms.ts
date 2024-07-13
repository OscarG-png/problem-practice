function canVisitAllRooms(rooms: number[][]): boolean {
  let visited = new Set<number>();

  function dfs(room: number) {
    visited.add(room);
    for (let key of rooms[room]) {
      if (!visited.has(key)) {
        dfs(key);
      }
    }
  }
  dfs(0);
  return visited.size === rooms.length;
}
