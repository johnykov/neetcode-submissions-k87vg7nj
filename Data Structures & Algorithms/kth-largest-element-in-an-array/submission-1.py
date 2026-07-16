import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int: 
        if not nums:
            return None
        pivot = random.choice(nums)
        less = []
        equal = []
        greater = []
        for i in nums:
            if i > pivot:
                greater.append(i)
            elif i < pivot:
                less.append(i)
            else:
                equal.append(i)

        if k <= len(greater):
            return self.findKthLargest(greater, k)
        elif k <= len(greater) + len(equal):
            return pivot
        else:
            return self.findKthLargest(less, k - len(greater) - len(equal))