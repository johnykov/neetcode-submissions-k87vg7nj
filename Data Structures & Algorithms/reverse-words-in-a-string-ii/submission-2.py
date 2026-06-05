class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        last = -1
        for i in range(len(s)):
            if s[i] == " ":
                l = last + 1
                r = i - 1
                while l < r:
                    s[l], s[r] = s[r], s[l]
                    l += 1
                    r -= 1 
                last = i
        l = last + 1
        r = len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1 
        