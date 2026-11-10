class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [0] * length
        prefix_arr = [0] * length
        suffix_arr = [0] * length

        prefix_arr[0] = suffix_arr[length - 1] = 1
        for i in range (1, length):
            prefix_arr[i] = nums[i - 1] * prefix_arr[i - 1]
        for i in range (length - 2, -1, -1):
            suffix_arr[i] = nums[i + 1] * suffix_arr[i + 1]
        
        for i in range(length):
            res[i] = prefix_arr[i] * suffix_arr[i]

        return res