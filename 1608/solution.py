from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        candidate = len(nums)
        prev = -1
        for offset, num in enumerate(nums):
            if prev >= candidate - offset:
                return -1
            prev = num
            if num >= candidate - offset:
                return candidate - offset
        return -1


if __name__ == '__main__':
    assert Solution().specialArray([3, 5]) == 2
    assert Solution().specialArray([0, 0]) == -1
    assert Solution().specialArray([0, 4, 3, 0, 4]) == 3
    assert Solution().specialArray([0, 3, 3, 3, 4]) == -1

