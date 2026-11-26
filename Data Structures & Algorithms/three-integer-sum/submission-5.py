class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # find 3 elements whose sum == 0
        # all of them should be different. meaning no 2 elements in the output array be same.
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i-1]: # if we find duplicates
                continue
            l,r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res
