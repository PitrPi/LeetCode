from functools import reduce
from typing import List


class Solution:
    def get_bitwise(self, a, b):
        return a ^ b

    def naive_count_triplets(self, arr: List[int]) -> int:
        count = 0
        for k in range(1, len(arr)):
            b = reduce(self.get_bitwise, arr[1 : (k + 1)])
            for j in range(1, k + 1):
                a = reduce(self.get_bitwise, arr[0:j])
                for i in range(j):
                    if a == b:
                        count += 1
                    a ^= arr[i]
                b ^= arr[j]
        return count
