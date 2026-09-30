class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashM = {}

        for i, num in enumerate(nums):
            needed = target - num
            if needed in hashM:
                return [hashM[needed], i]
            hashM[num] = i 