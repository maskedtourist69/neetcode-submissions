class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        storage = set(nums)
        if len(nums) == len(storage):
            return False
        return True