class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        storage = []
        for num in nums:
            if num not in storage:
                storage.append(num)
            else:
                return True
        return False