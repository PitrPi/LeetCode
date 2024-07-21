from collections import deque
from typing import List


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row = self.order(k, rowConditions)
        col = self.order(k, colConditions)
        if not row or not col:
            return []
        res = [[0] * k for _ in range(k)]
        for i in range(k):
            for j in range(k):
                if row[i] == col[j]:
                    res[i][j] = row[i]
        return res

    def order(self, k, cons):
        degree = [0] * (k + 1)
        adjacent = [[] for _ in range(k + 1)]
        res = []
        for con in cons:
            degree[con[1]] += 1
            adjacent[con[0]].append(con[1])
        deck = deque()
        for i in range(1, k + 1):
            if degree[i] == 0:
                deck.append(i)
        while deck:
            k -= 1
            node = deck.popleft()
            res.append(node)
            for next_node in adjacent[node]:
                degree[next_node] -= 1
                if degree[next_node] == 0:
                    deck.append(next_node)

        return res if k == 0 else []


if __name__ == "__main__":
    k = 3
    rowConditions = [[1, 2], [2, 3], [3, 1], [2, 3]]
    colConditions = [[1, 2]]
    s = Solution()
    print(s.buildMatrix(k, rowConditions, colConditions))

    k = 3
    rowConditions = [[1, 2], [3, 2]]
    colConditions = [[2, 1], [3, 2]]
    s = Solution()
    print(s.buildMatrix(k, rowConditions, colConditions))
