import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]
        pivot = random.choice(nums)
        less = [i for i in nums if i < pivot]
        greater = [i for i in nums if i > pivot]

        equal_count = len(nums) - len(less) - len(greater)

        if k <= len(greater):
            return self.findKthLargest(greater, k)
        if k <= equal_count + len(greater):
            return pivot
        return self.findKthLargest(less, k - len(greater) - equal_count)