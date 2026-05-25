class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        dists = [abs(x - num) for num in arr]
        min_idx = dists.index(min(dists))
        l, r = min_idx, min_idx

        for _ in range(k - 1):
            if l > 0 and r < len(arr) - 1 and dists[l - 1] <= dists[r+1]:
                l -= 1
            elif r < len(arr) - 1:
                r += 1
            elif l > 0:
                l -= 1
        # print(l, r)
        return arr[l:r + 1]