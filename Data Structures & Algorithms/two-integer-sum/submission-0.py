class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_cache = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_cache:
                return [num_cache[complement], i]
            num_cache[num] = i
        