class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        prefix = {0:1}
        for num in nums:
            current_sum += num
            difference = current_sum - k
            if difference in prefix:
                count += prefix[difference]
            prefix[current_sum] = prefix.get(current_sum, 0) + 1
        return count