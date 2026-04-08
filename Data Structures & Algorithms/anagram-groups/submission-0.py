class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {} #or defalutdict

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')] +=1
            if tuple(count) not in res: 
                # defaultdict is a sinctactic sugar for this condition
                res[tuple(count)]=[]
            res[tuple(count)].append(s)
            # tuple is native python
        return list(res.values())
        