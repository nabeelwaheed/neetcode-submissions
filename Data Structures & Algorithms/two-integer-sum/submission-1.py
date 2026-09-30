class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, number in enumerate(nums):
            needed = target - number
            if needed in hashmap:
                return [hashmap[needed], index]
            hashmap[number] = index
        return []
