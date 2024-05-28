from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = max_price = diff = -1
        for price in prices:
            if min_price < 0 or price < min_price:
                min_price = price
                max_price = -1
            if max_price < 0 or price > max_price:
                max_price = price
            if max_price - min_price > diff:
                diff = max_price - min_price
        return diff
