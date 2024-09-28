import copy
from collections import defaultdict
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        cum_sum = defaultdict(set)  # sum: set of combinations
        for c in candidates:
            new_cum_sum = copy.deepcopy(cum_sum)
            for k, v in cum_sum.items():
                if k + c <= target:
                    new_cum_sum[k + c] |= set([tuple(sorted(one + (c,))) for one in v])
            new_cum_sum[c] |= {(c,)}
            cum_sum = new_cum_sum
        return [list(x) for x in cum_sum[target]]


if __name__ == "__main__":
    candidates = [2, 5, 2, 1, 2]
    target = 5
    Solution().combinationSum2(candidates, target)
