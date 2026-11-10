class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr = [0] * len(nums)
        suffix_arr = [0] * len(nums)

        temp = 1
        for i in range(len(nums)):
            prefix_arr[i] = temp
            temp *= nums[i]
        
        temp = 1
        i = len(nums) - 1
        while i >= 0:
            suffix_arr[i] = temp
            temp *= nums[i]
            i -= 1
        
        res = []
        for i in range(len(nums)):
            res.append(prefix_arr[i] * suffix_arr[i])

        return res