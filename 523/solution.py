from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        history = {0: -1}  # Zero is good mod
        running_mod = 0
        for idx in range(len(nums)):
            running_mod = (running_mod + nums[idx]) % k
            if running_mod in history and idx - history[running_mod] > 1:
                return True
            if running_mod not in history:
                history[running_mod] = idx


if __name__ == "__main__":
    nums = [23, 2, 4, 6, 6]
    k = 7
    print(Solution().checkSubarraySum(nums, k))
