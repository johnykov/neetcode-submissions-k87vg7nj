class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(l, r):
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
    
        reverse(0, len(s)-1)

        last = -1
        for i in range(len(s)):
            if s[i] == " ":
                reverse(last+1, i -1)
                last = i

        reverse(last + 1, len(s) -1 )
        