class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        end = -1
        res = 0

        for pocz in range(len(s)):
            while end + 1 < len(s) and freq.get(s[end + 1], 0) == 0:
                end += 1
                freq[s[end]] = freq.get(s[end],0) + 1
            freq[s[pocz]] -=1
            res = max(res, end - pocz + 1)
        return res 