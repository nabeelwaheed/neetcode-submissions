class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            b = i + 1
            c = len(nums) - 1
            while b < c:
                cur_sum = n + nums[b] + nums[c]
                if cur_sum > 0:
                    c -= 1
                elif cur_sum < 0:
                    b += 1
                else:
                    res.append([n, nums[b], nums[c]])
                    b += 1
                    while nums[b] == nums[b - 1] and b < c:
                        b += 1
        return res

            

        