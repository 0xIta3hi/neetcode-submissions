class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # we start with one pointer at beginning and one at the end of the list
        # as we move we add each element and check if sum == target ? true : false.
        left = 0
        right = len(numbers) -1
        while left < right:
            cursum = numbers[left] + numbers[right]
            if cursum > target:
                right -= 1
            elif cursum < target:
                left += 1
            else:
                return [left + 1, right + 1]
        return []
