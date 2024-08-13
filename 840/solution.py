from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if self.is_magic(grid, row, col):
                    res += 1
        return res

    def is_magic(self, grid, row, col):
        if set([x for c in grid[row:(row+3)] for x in c[col:(col+3)]]) != set(range(1, 10)):
            return False

        # rows
        for i in range(3):
            if sum(grid[row + i][col:(col+3)]) != 15:
                return False

        # cols
        for i in range(3):
            if sum([c[col+i] for c in grid[row:(row+3)]]) != 15:
                return False

        # diagonals
        if sum(grid[row+i][col+i] for i in range(3)) != 15:
            return False

        if sum(grid[row+i][col+2-i] for i in range(3)) != 15:
            return False

        return True


if __name__ == "__main__":
    grid = [[9, 0, 8, 1, 6], [2, 4, 3, 5, 7], [4, 3, 4, 9, 2], [2, 4, 5, 6, 1], [9, 8, 0, 7, 8]]

    s = Solution()
    print(s.numMagicSquaresInside(grid))
