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
        # use -1 as a sentinel so word starts are spaces[i] + 1
        spaces = [-1]
        for i in range(len(s)):
            if s[i] == " ":
                spaces.append(i)
        spaces.append(len(s))
        for i in range(len(spaces) - 1):
            # start after the previous space
            l = spaces[i] + 1
            r = spaces[i + 1] - 1
            # print(l, r)
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        