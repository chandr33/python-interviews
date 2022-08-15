from typing import List


class Islands:
    def __init__(self, islands: List[List[int]]):
        self.islands = islands
        self.rows, self.cols = len(islands), len(islands[0])
        self.visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]

    def is_valid(self, row, col) -> bool:
        return self.rows > row >= 0 and self.cols > col >= 0 and self.islands[row][col] == 1 and not self.visited[row][col]

    def count_islands(self) -> int:
        def dfs(row, col):
            self.visited[row][col] = True
            row_coord = [-1, -1, -1, 0, 0, 1, 1, 1]
            col_coord = [-1, 0, 1, -1, 1, -1, 0, 1]
            for i in range(8):
                next_row, next_col = row+row_coord[i], col+col_coord[i]
                if self.is_valid(next_row, next_col):
                    dfs(next_row, next_col)

        count = 0
        for i in range(len(self.islands)):
            for j in range(len(self.islands[0])):
                if self.islands[i][j] == 1 and not self.visited[i][j]:
                    count += 1
                    dfs(i, j)

        return count


if __name__ == '__main__':
    """
    Given a grid of size n*m (n is the number of rows and m is the number of columns in the grid) consisting of '0's 
    (Water) and '1's(Land). Find the number of islands.

    Note: An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically or 
    diagonally i.e., in all 8 directions.
    """

    grid_1 = [[0, 1], [1, 0], [1, 1], [1, 0]]
    grid_2 = [[0, 1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 0, 1, 0]]

    island = Islands(islands=grid_2)
    print(island.count_islands())
