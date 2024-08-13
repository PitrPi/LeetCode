import copy
from typing import List


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        self.len_x = len(grid)
        self.len_y = len(grid[0])
        land_tiles = sum([sum(x) for x in grid])

        grid_count = copy.deepcopy(grid)
        island_size = self.find_start(grid_count)
        print(island_size, land_tiles)
        if island_size != land_tiles:
            return 0
        if land_tiles == 2:
            return 2
        if land_tiles == 1:
            return 1

        for x in range(self.len_x):
            for y in range(self.len_y):
                if grid[x][y] == 1:
                    grid[x][y] = 0
                    grid_count = copy.deepcopy(grid)
                    island_size = self.find_start(grid_count)
                    if island_size != (land_tiles - 1):
                        print(x, y)
                        return 1
                    grid[x][y] = 1
        return 2

    def find_start(self, grid):
        for idxx, x in enumerate(grid):
            for idxy, y in enumerate(x):
                if y == 1:
                    return self.fill_island(grid, idxx, idxy)

    def fill_island(self, grid, x, y):
        counter = 0
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        stack = [(x, y)]
        while stack:
            curr_x, curr_y = stack.pop()
            if grid[curr_x][curr_y] == 1:
                counter += 1
            grid[curr_x][curr_y] = 0

            for d in dirs:
                if (
                    0 <= curr_x + d[0] < self.len_x
                    and 0 <= curr_y + d[1] < self.len_y
                    and grid[curr_x + d[0]][curr_y + d[1]] == 1
                ):
                    stack.append((curr_x + d[0], curr_y + d[1]))

        return counter
