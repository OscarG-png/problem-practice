from typing import List

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])

        max_of_row_mins = float('-inf')
        for r in range(ROWS):
            row_mins = min(matrix[r])
            max_of_row_mins = max(row_mins, max_of_row_mins)

        for c in range(COLS):
            col_max = matrix[0][c]

            for r in range(ROWS):
                col_max = max(col_max, matrix[r][c])
            if col_max == max_of_row_mins:
                return [col_max]

        return []
