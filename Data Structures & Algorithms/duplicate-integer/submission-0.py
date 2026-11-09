class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen.values():
                return True
            seen[i] = nums[i]
        return False