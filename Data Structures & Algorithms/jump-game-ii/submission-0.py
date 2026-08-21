class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [n] * n
        dp[0] = 0
        for i in range(n):
            for skok in range(1, nums[i] + 1):
                if i + skok < n:
                    dp[i+skok] = min(dp[i+skok], dp[i]+1)
        return dp[n-1]