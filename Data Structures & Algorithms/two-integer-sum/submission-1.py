class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_to_idx = defaultdict(int)
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in diff_to_idx:
                return [diff_to_idx[diff], idx]
            diff_to_idx[num] = idx
        # return []