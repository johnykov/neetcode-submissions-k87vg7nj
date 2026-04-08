class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = defaultdict(int)
        res, r = 0,-1
        for l in range(len(s)):
            while r + 1 < len(s) and mp[s[r+1]] == 0:
                r+=1
                mp[s[r]] = mp[s[r]] + 1
            mp[s[l]] -= 1
            res = max(res, r - l + 1)
        return res