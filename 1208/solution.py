class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # map everything to ascii
        s = [ord(x) for x in s]
        t = [ord(x) for x in t]
        diff = [abs(x - y) for x, y in zip(s, t)]
        p1 = p2 = cusum = length = 0
        while p2 < len(diff):
            if cusum + diff[p2] <= maxCost:
                cusum += diff[p2]
                p2 += 1
                length = max(length, p2 - p1)
            else:
                cusum -= diff[p1]
                p1 += 1
                if p1 > p2:
                    p2 = p1
                    cusum = 0
        return length


if __name__ == "__main__":
    assert Solution().equalSubstring("abcd", "cdef", 1) == 0
