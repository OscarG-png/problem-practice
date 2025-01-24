function eventualSafeNodes(graph: number[][]): number[] {
	const n = graph.length;
	let safe = new Map<number, boolean>();

	function dfs(i: number) {
		if (safe.has(i)) return safe.get(i);
		safe.set(i, false);
		for (const neih of graph[i]) {
			if (!dfs(neih)) return safe.get(i);
		}
		safe.set(i, true);
		return true;
	}

	let res: number[] = [];
	for (let i = 0; i < n; i++) {
		if (dfs(i)) res.push(i);
	}

	return res;
}
