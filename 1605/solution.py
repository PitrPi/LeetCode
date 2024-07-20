from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        res = [[0] * len(colSum) for _ in range(len(rowSum))]
        for row in range(len(rowSum)):
            for col in range(len(colSum)):
                res[row][col] = min(rowSum[row], colSum[col])
                rowSum[row] -= res[row][col]
                colSum[col] -= res[row][col]

        return res


if __name__ == "__main__":
    rowSum = [3, 8]
    colSum = [4, 7]
    print(Solution().restoreMatrix(rowSum, colSum))
