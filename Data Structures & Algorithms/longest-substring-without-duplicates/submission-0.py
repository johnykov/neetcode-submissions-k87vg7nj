class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        L=0
        res=0

        for R, char in enumerate(s):
            while char in char_set:
                char_set.remove(s[L])
                L+=1
            char_set.add(char)
            res=max(res, R-L+1)
        return res
        