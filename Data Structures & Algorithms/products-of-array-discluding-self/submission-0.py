class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        product = 1

        # Pass 1: Calculate products to the left
        for i in range(n):
            result[i] = product
            product *= nums[i]

        # Pass 2: Calculate products to the right
        product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= product
            product *= nums[i]

        return result