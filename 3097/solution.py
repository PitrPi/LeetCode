class Solution:
    def minimumSubarrayLength(self, nums, k):
        n = len(nums)
        bit_count = [0] * 32
        curr = 0
        left = 0
        res = float("inf")

        for right in range(n):
            curr |= nums[right]

            for bit in range(32):
                if nums[right] & (1 << bit):
                    bit_count[bit] += 1

            while left <= right and curr >= k:
                res = min(res, right - left + 1)

                curr_new = 0
                for bit in range(32):
                    if nums[left] & (1 << bit):
                        bit_count[bit] -= 1
                    if bit_count[bit] > 0:
                        curr_new |= 1 << bit

                curr = curr_new
                left += 1

        return res if res != float("inf") else -1


if __name__ == "__main__":
    nums = [2, 1, 8]
    k = 10
    print(Solution().minimumSubarrayLength(nums, k))
