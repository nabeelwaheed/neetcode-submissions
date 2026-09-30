class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = 1
        for i in range(len(nums)):
            res.append(prefix)
            prefix *= nums[i]
        
        posfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= posfix
            posfix *= nums[i]
        return res