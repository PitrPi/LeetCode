from collections import deque
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        small = deque()
        big = deque()
        left = res = 0
        for idx, nu in enumerate(nums):
            while small and small[-1] > nu:
                small.pop()
            small.append(nu)
            while big and big[-1] < nu:
                big.pop()
            big.append(nu)
            while big[0] - small[0] > limit:
                if big[0] == nums[left]:
                    big.popleft()
                if small == nums[left]:
                    small.popleft()
                left += 1
            res = max(res, idx - left + 1)
        return res
