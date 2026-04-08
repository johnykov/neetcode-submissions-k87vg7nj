class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_prof = float("Inf"),0
        for price in prices:
            min_price = min(min_price, price)
            max_prof = max(max_prof, price-min_price)
        return max_prof
        