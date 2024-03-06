import unittest


def possible_paths(grid, robotLocation, maxSteps):
    rows = len(grid)
    cols = len(grid[0])

    def validMove(row, col):
        return 0 <= row < rows and 0 <= col < cols and grid[row][col] != "X"

    def dfs(row, col, steps):
        if grid[row][col] == "C":
            return 1
        if steps == 0:
            return 0
        count = 0
        grid[row][col] = "X"
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_row = row + dr
            new_col = col + dc
            if validMove(new_row, new_col):
                count += dfs(new_row, new_col, steps - 1)
        grid[row][col] = "0"
        return count
    start_row, start_col = robotLocation
    return dfs(start_row, start_col, maxSteps)


class TestPossiblePaths(unittest.TestCase):
    def test_possible_paths(self):
        grid = [
            ['0', '0', '0', '0', '0', '0', 'X', 'C'],
            ['0', '0', '0', '0', 'C', '0', 'X', 'X'],
            ['0', '0', 'S', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', 'C', 'X']
        ]
        robotLocation = [2, 2]
        maxSteps = 3
        result = possible_paths(grid, robotLocation, maxSteps)
        expected_result = 3
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
